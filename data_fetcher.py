# data_fetcher.py

import yfinance as yf
import pandas as pd

def fetch_stock_data(stock_symbols: str, period: str = '1mo', interval: str = '1d'):
    """
    Fetch stock data for multiple stock symbols.
    Args:
        stock_symbols (str): Comma-separated stock symbols (e.g., 'RELIANCE.NS,TCS.NS').
        period (str): Data period (e.g., '1mo', '3mo', etc.).
        interval (str): Data interval (e.g., '1d', '1h', etc.).
    Returns:
        pd.DataFrame: DataFrame containing stock data for all symbols.
    """
    data = yf.download(tickers=stock_symbols, period=period, interval=interval, group_by='ticker')
    return data
