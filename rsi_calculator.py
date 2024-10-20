import pandas as pd

def calculate_rsi(data, window=14):
    """
    Calculate the Relative Strength Index (RSI) from stock data.
    Args:
    - data (DataFrame): The stock data containing 'Close' prices.
    - window (int): The window size for RSI calculation (default is 14).

    Returns:
    - pandas Series: The RSI values.
    """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi
