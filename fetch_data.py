import yfinance as yf
import pandas as pd
from datetime import datetime
import os

# Indian Stocks we're focusing on (with .NS for NSE)
STOCKS = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFC.NS", "ICICIBANK.NS"]

# Date range
START_DATE = "2018-01-01"
END_DATE = datetime.now().strftime('%Y-%m-%d')  # Use current date as the end date

def download_stock_data(ticker):
    try:
        print(f"Fetching data for {ticker}...")
        data = yf.download(ticker, start=START_DATE, end=END_DATE)
        if data.empty:
            print(f"No data found for {ticker}.")
            return

        # Save data to CSV
        file_path = f"data/{ticker}.csv"
        data.to_csv(file_path)
        print(f"Data for {ticker} saved to {file_path}")
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")

if __name__ == "__main__":
    # Make sure 'data' folder exists
    if not os.path.exists("data"):
        os.makedirs("data")

    # Fetch data for each stock
    for stock in STOCKS:
        download_stock_data(stock)
