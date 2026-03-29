import pandas as pd
from sqlalchemy.orm import Session
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.db.database import engine, SessionLocal, Base
from src.db.models import PassengerTraffic

# To read CSV from https use path: 'https://data.sfgov.org/api/v3/views/rkru-6vcg/query.csv' 
RAW_DATA_PATH = 'data/raw/Air_Traffic_Passenger_Statistics.csv'

def extract_and_transform(filepath: str) -> pd.DataFrame:
    print(f'Reading raw Data from {filepath}...')
    df = pd.read_csv(filepath)

    columns_to_keep = [
        "Activity Period", "Activity Period Start Date", "Operating Airline",
        "GEO Summary", "GEO Region", "Activity Type Code", 
        "Price Category Code", "Passenger Count"
    ]
    df = df[columns_to_keep]

    df.columns = [
        "activity_period", "activity_period_start_date", "operating_airline",
        "geo_summary", "geo_region", "activity_type_code", 
        "price_category_code", "passenger_count"
    ]
    df["activity_period_start_date"] = pd.to_datetime(df["activity_period_start_date"]).dt.date
    
    print(f"Transformed {len(df)} rows.")
    return df

def load_to_db(df: pd.DataFrame) -> None:
    print('Creating DB tables...')
    Base.metadata.create_all(bind=engine)

    print('Loading data to PostgreSQL...')
    df.to_sql('passenger_traffic', con=engine, if_exists='append', index=False)
    print('Data loaded successfully!')

if __name__ == '__main__':
    transformed_data = extract_and_transform(RAW_DATA_PATH)
    load_to_db(transformed_data)