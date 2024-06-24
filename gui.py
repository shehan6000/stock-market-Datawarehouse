import tkinter as tk
from tkinter import ttk
import pandas as pd
from sqlalchemy import create_engine

# Replace the placeholders with your actual database credentials
username = 'root'
password = '40964101'
host = 'localhost'  # For example, 'localhost' or an IP address
port = 3306  # Default MySQL port
database = 'stock_market'

# Create the engine with the actual credentials
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# Rest of your code...


# Function to fetch data from the database
def fetch_data():
    query = "SELECT * FROM StockPrices"
    df = pd.read_sql(query, con=engine)
    return df

# Function to display data in the GUI
def display_data():
    df = fetch_data()
    for i, row in df.iterrows():
        tree.insert("", "end", values=list(row))

# Create the main window
root = tk.Tk()
root.title("Stock Market Data Warehouse")

# Create a treeview to display the data
tree = ttk.Treeview(root, columns=("stock_id", "date_id", "open_price", "close_price", "high_price", "low_price", "volume"), show="headings")
tree.heading("stock_id", text="Stock ID")
tree.heading("date_id", text="Date ID")
tree.heading("open_price", text="Open Price")
tree.heading("close_price", text="Close Price")
tree.heading("high_price", text="High Price")
tree.heading("low_price", text="Low Price")
tree.heading("volume", text="Volume")
tree.pack(fill=tk.BOTH, expand=True)

# Fetch and display data on button click
button = tk.Button(root, text="Load Data", command=display_data)
button.pack()

# Run the application
root.mainloop()
