import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="supply_chain",
    user="postgres",
    password = os.getenv("DB_PASSWORD")
)

print("Connection successful")

conn.close()