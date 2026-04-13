import psycopg2
import os
from dotenv import load_dotenv

load_dotenv("credentials.env")

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("host"),
        port=5432,
        database="dev",
        user=os.getenv("user"),
        password=os.getenv("password"),
        sslmode="require",
        options="-c search_path=country_profiles"
    )
    return conn

