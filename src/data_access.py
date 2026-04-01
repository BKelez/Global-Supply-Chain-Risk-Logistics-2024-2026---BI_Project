import psycopg2
import pandas as pd


def get_connection():

    conn = psycopg2.connect(
        host="localhost",
        database="supply_chain",
        user="postgres",
        password = os.getenv("DB_PASSWORD")
    )

    return conn


def query_to_dataframe(query):

    conn = get_connection()

    df = pd.read_sql(query, conn)

    conn.close()

    return df