import requests
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base

# Fix the deprecation warning
Base = declarative_base()

class StockPrices(Base):
    __tablename__ = 'StockPrices'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    volume = Column(Integer)

# Database connection credentials
username = 'root'
password = '40964101'
host = 'localhost'  # For example, 'localhost' or an IP address
port = 3306  # Default MySQL port
database = 'stock_market'

# Database connection URL
db_url = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

# Create the SQLAlchemy engine
engine = create_engine(db_url)

# Create the table(s) in the database
Base.metadata.create_all(engine)

# Function to extract data from an API
def extract_data(api_url, params):
    response = requests.get(api_url, params=params)
    data = response.json()
    return pd.DataFrame(data['Time Series (Daily)']).transpose()

# Function to transform data
def transform_data(df):
    df.reset_index(inplace=True)
    df.columns = ['date', 'open_price', 'high_price', 'low_price', 'close_price', 'volume']
    df['date'] = pd.to_datetime(df['date'])
    df['open_price'] = df['open_price'].astype(float)
    df['high_price'] = df['high_price'].astype(float)
    df['low_price'] = df['low_price'].astype(float)
    df['close_price'] = df['close_price'].astype(float)
    df['volume'] = df['volume'].astype(int)
    return df

# Function to load data into the database
def load_data(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists='append', index=False)

# API endpoint and parameters
api_url = 'https://www.alphavantage.co/query'
params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'AAPL',
    'apikey': '497N07BL33P5TD14'
}

# Extract data
stock_data = extract_data(api_url, params)

# Transform data
stock_data = transform_data(stock_data)

# Load data
load_data(stock_data, 'StockPrices', engine)

print("ETL process completed successfully.")
