import pandas as pd
import psycopg2

# -----------------------------
# PostgreSQL Verbindung
# -----------------------------

conn = psycopg2.connect(
    host="localhost",
    database="supply_chain",
    user="postgres",
    password = os.getenv("DB_PASSWORD")  
)

cursor = conn.cursor()

print("Connected to database")

# -----------------------------
# CSV laden
# -----------------------------

df = pd.read_csv("data/raw/global_supply_chain_risk_2026.csv")

print("Dataset loaded")


# -----------------------------
# DIM PORT
# -----------------------------

ports = pd.concat([
    df["Origin_Port"],
    df["Destination_Port"]
]).unique()

for port in ports:
    cursor.execute("""
        INSERT INTO dim_port (port_name)
        VALUES (%s)
        ON CONFLICT DO NOTHING
    """, (port,))

print("dim_port loaded")


# -----------------------------
# DIM TRANSPORT MODE
# -----------------------------

transport_modes = df["Transport_Mode"].unique()

for mode in transport_modes:
    cursor.execute("""
        INSERT INTO dim_transport_mode (transport_mode)
        VALUES (%s)
        ON CONFLICT DO NOTHING
    """, (mode,))

print("dim_transport_mode loaded")


# -----------------------------
# DIM PRODUCT CATEGORY
# -----------------------------

categories = df["Product_Category"].unique()

for cat in categories:
    cursor.execute("""
        INSERT INTO dim_product_category (product_category)
        VALUES (%s)
        ON CONFLICT DO NOTHING
    """, (cat,))

print("dim_product_category loaded")


# -----------------------------
# DIM WEATHER
# -----------------------------

weather_conditions = df["Weather_Condition"].unique()

for weather in weather_conditions:
    cursor.execute("""
        INSERT INTO dim_weather (weather_condition)
        VALUES (%s)
        ON CONFLICT DO NOTHING
    """, (weather,))

print("dim_weather loaded")


# -----------------------------
# DIM DATE
# -----------------------------

df["Date"] = pd.to_datetime(df["Date"])

dates = df["Date"].dt.date.unique()

for d in dates:

    year = pd.to_datetime(d).year
    month = pd.to_datetime(d).month
    quarter = (month - 1) // 3 + 1

    cursor.execute("""
        INSERT INTO dim_date (date, year, month, quarter)
        VALUES (%s,%s,%s,%s)
        ON CONFLICT DO NOTHING
    """, (d, year, month, quarter))

print("dim_date loaded")


# -----------------------------
# LOAD FACT TABLE
# -----------------------------

print("Loading fact table...")

for index, row in df.iterrows():

    # Date ID
    cursor.execute(
        "SELECT date_id FROM dim_date WHERE date = %s",
        (row["Date"].date(),)
    )
    date_id = cursor.fetchone()[0]

    # Origin Port ID
    cursor.execute(
        "SELECT port_id FROM dim_port WHERE port_name = %s",
        (row["Origin_Port"],)
    )
    origin_port_id = cursor.fetchone()[0]

    # Destination Port ID
    cursor.execute(
        "SELECT port_id FROM dim_port WHERE port_name = %s",
        (row["Destination_Port"],)
    )
    destination_port_id = cursor.fetchone()[0]

    # Transport Mode ID
    cursor.execute(
        "SELECT transport_mode_id FROM dim_transport_mode WHERE transport_mode = %s",
        (row["Transport_Mode"],)
    )
    transport_mode_id = cursor.fetchone()[0]

    # Product Category ID
    cursor.execute(
        "SELECT product_category_id FROM dim_product_category WHERE product_category = %s",
        (row["Product_Category"],)
    )
    product_category_id = cursor.fetchone()[0]

    # Weather ID
    cursor.execute(
        "SELECT weather_id FROM dim_weather WHERE weather_condition = %s",
        (row["Weather_Condition"],)
    )
    weather_id = cursor.fetchone()[0]

    # Insert Fact Table
    cursor.execute("""
        INSERT INTO fact_shipments (
            shipment_id,
            date_id,
            origin_port_id,
            destination_port_id,
            transport_mode_id,
            product_category_id,
            weather_id,
            distance_km,
            weight_mt,
            fuel_price_index,
            geopolitical_risk_score,
            carrier_reliability_score,
            lead_time_days,
            disruption_occurred
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        row["Shipment_ID"],
        date_id,
        origin_port_id,
        destination_port_id,
        transport_mode_id,
        product_category_id,
        weather_id,
        row["Distance_km"],
        row["Weight_MT"],
        row["Fuel_Price_Index"],
        row["Geopolitical_Risk_Score"],
        row["Carrier_Reliability_Score"],
        row["Lead_Time_Days"],
        row["Disruption_Occurred"]
    ))

print("fact_shipments loaded")

# -----------------------------
# Commit & Close
# -----------------------------

conn.commit()

cursor.close()
conn.close()

print("ETL for dimension tables finished")