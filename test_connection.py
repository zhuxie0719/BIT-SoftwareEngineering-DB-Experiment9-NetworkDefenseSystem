from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

DB_CONFIG = {
    "host": "",
    "port": 26000,
    "dbname": "postgres",
    "user": "omm",
    "password": "",
}

# Correct URI format with hostaddr in query string
db_uri = (
    f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
    f"?hostaddr={DB_CONFIG['host']}"
)

try:
    engine = create_engine(db_uri)
    with engine.connect():
        print("Connection successful!")
except OperationalError as e:
    print(f"Connection failed: {e}")
    