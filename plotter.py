# plotter.py

import matplotlib.pyplot as plt

def plot_stock_and_rsi(data, rsi, save_path='static/stock_plot.png'):
    """
    Plot the stock prices and RSI values, and save the plot to an image file.

    Args:
    - data (DataFrame): Stock data with 'Close' prices.
    - rsi (Series): RSI values calculated from stock prices.
    - save_path (str): File path to save the plot.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Plot stock price
    ax1.plot(data.index, data['Close'], label='Stock Price')
    ax1.set_title("Stock Price")
    ax1.set_ylabel("Price")
    ax1.legend()

    # Plot RSI
    ax2.plot(rsi.index, rsi, label='RSI', color='orange')
    ax2.axhline(70, color='red', linestyle='--', label='Overbought')
    ax2.axhline(30, color='green', linestyle='--', label='Oversold')
    ax2.set_title("Relative Strength Index (RSI)")
    ax2.set_ylabel("RSI")
    ax2.legend()

    # Save the plot to the file
    plt.savefig(save_path)
    plt.close()
