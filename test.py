# another_script.py

from db import get_db_connection

def list_tables():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT * from test;
        """)
        
        tables = cur.fetchall()
        for schema, table in tables:
            print(f"{schema}.{table}")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error listing tables: {e}")

if __name__ == "__main__":
    list_tables()
