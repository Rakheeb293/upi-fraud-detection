from sqlalchemy import create_engine, MetaData
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define connection URLs
sqlite_url = "sqlite:///instance/users.db"
postgres_url = os.getenv("DATABASE_URL")

if not postgres_url:
    raise ValueError("DATABASE_URL not set in .env")

# Connect engines
sqlite_engine = create_engine(sqlite_url)
postgres_engine = create_engine(postgres_url)

# Reflect tables from SQLite
metadata = MetaData()
metadata.reflect(bind=sqlite_engine)

print(f"Found tables: {list(metadata.tables.keys())}")

# Transfer each table
for table_name in metadata.tables:
    print(f"Transferring table: {table_name}")
    df = pd.read_sql_table(table_name, sqlite_engine)
    df.to_sql(table_name, postgres_engine, if_exists='append', index=False)

print("✅ Migration complete!")
