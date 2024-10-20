from flask import Flask, render_template, request
from data_fetcher import fetch_stock_data
from indicator_calculator import calculate_rsi
from plotter import plot_stock_and_rsi
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    stock_symbol = request.form.get('stock_symbol').upper()  # Get stock symbol from the form
    stock_data = fetch_stock_data(stock_symbol, period='1mo', interval='1d')
    
    if stock_data.empty:
        return render_template('index.html', error="No data found for the given stock symbol.")
    
    rsi = calculate_rsi(stock_data)
    
    if not os.path.exists('static'):
        os.makedirs('static')

    # Save the plot as an image file
    plot_path = f'static/{stock_symbol}_plot.png'
    plot_stock_and_rsi(stock_data, rsi, save_path=plot_path)
    
    return render_template('index.html', plot=f'{stock_symbol}_plot.png', symbol=stock_symbol)

if __name__ == '__main__':
    app.run(debug=True)
