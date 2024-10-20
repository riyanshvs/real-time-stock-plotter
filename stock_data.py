import yfinance as yf

def fetch_stock_data(stock_symbol, period='1mo', interval='1d'):
    """
    Fetch real-time stock data for a given symbol.
    Args:
    - stock_symbol (str): The stock symbol to fetch data for.
    - period (str): The time period of data (e.g., '1mo', '1d').
    - interval (str): The interval for data points (e.g., '1m', '1d').
    
    Returns:
    - pandas DataFrame containing stock data.
    """
    data = yf.download(stock_symbol, period=period, interval=interval)
    return data
