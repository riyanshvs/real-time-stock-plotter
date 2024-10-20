# indicator_calculator.py

import pandas as pd

def calculate_rsi(data: pd.DataFrame, window_length: int = 14) -> pd.Series:
    """
    Calculate the Relative Strength Index (RSI) for a given stock data.

    Parameters:
        data (pd.DataFrame): DataFrame containing 'Close' prices.
        window_length (int): The window length for calculating RSI.

    Returns:
        pd.Series: A pandas Series containing the RSI values.
    """
    delta = data['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=window_length, min_periods=window_length).mean()
    avg_loss = loss.rolling(window=window_length, min_periods=window_length).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi.fillna(0)
