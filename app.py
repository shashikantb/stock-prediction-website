from flask import Flask, render_template, request, jsonify
import yfinance as yf
import numpy as np
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict")
def predict():
    ticker = request.args.get("ticker", "AAPL")
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")

    if hist.empty:
        return jsonify({"error": "No data found"})

    prices = hist["Close"].tolist()
    dates = [d.strftime('%Y-%m-%d') for d in hist.index]

    # Simple prediction logic (mock)
    trend = "Up" if prices[-1] > prices[-2] else "Down"
    future_price = round(prices[-1] * (1.02 if trend == "Up" else 0.98), 2)
    moving_averages = [round(np.mean(prices[-d:]), 2) for d in (5, 10, 20)]

    return jsonify({
        "trend": trend,
        "future_price": future_price,
        "days": 5,
        "moving_averages": moving_averages,
        "dates": dates,
        "prices": prices
    })

if __name__ == "__main__":
    app.run(debug=True)
