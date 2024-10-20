# Real-Time Stock Chart Plotter and Prediction using RSI

This project fetches real-time stock data, calculates the Relative Strength Index (RSI), and plots both the stock prices and RSI values for analysis.

## Setup

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Run the project:
    ```
    python main.py
    ```

3. The project will fetch real-time stock data for Reliance Industries (NSE) and plot the stock price and RSI values.

## Files

- `main.py`: The main script to run the project.
- `stock_data.py`: Script to fetch real-time stock data.
- `rsi_calculator.py`: Script to calculate the RSI from stock prices.
- `plotter.py`: Script to plot stock data and RSI values.

## Dependencies

- Python 3.x
- yfinance
- pandas
- matplotlib
