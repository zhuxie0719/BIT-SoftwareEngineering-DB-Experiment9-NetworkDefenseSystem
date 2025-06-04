# test_connection.py
import psycopg2
from config import DB_CONFIG  # Import your config

try:
    # Attempt to connect
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
    )
    
    # Check if connection is successful
    if conn:
        print("✅ Connection successful!")
        
        # Optional: Execute a simple query
        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            print(f"Database version: {version[0]}")
        
        conn.close()  # Close the connection
    else:
        print("❌ Connection failed. No connection object returned.")

except psycopg2.Error as e:
    print(f"❌ Connection error: {e}")