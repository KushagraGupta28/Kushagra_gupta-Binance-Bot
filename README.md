# 🚀 Binance Futures Trading Bot

A Python-based interactive CLI bot that executes Binance **USDT-M Futures orders** in real time.  
Supports Market Orders, Limit Orders, and advanced strategies like **Stop-Limit**, **OCO**, **TWAP**, and **Grid Trading**.

---

## 📦 Features Implemented

### 🔹 Core Order Types
✔ Market Buy/Sell  
✔ Limit Buy/Sell  
✔ Stop-Limit Orders *(included inside `limit_orders.py`)*  

### 🔹 Advanced Order Systems (Bonus)
✔ OCO Orders *(One Cancels the Other)*  
✔ TWAP *(Time-Weighted Average Price Execution)*  
✔ Grid Strategy *(Auto buy-low / sell-high across levels)*  

---

## 🧱 Project Structure

Kushagra_Gupta_Binance_Bot/
├── .env # Stores API key + secret (DO NOT COMMIT)
├── bot.log # Log file saving both successful and failed orders
├── README.md # You are reading it :)
├── venv/ # Optional virtual environment
└── src/ # Source code
├── chatbot.py # CLI that takes interactive user input
├── client.py # Authenticated Binance client
├── market_orders.py # Market buy/sell functions
├── limit_orders.py # Limit + Stop-Limit functions
└── advanced/ # Advanced order strategies
├── oco.py # OCO dual-leg order handler
├── twap.py # TWAP execution engine
└── grid.py # Grid strategy execution


# -------------------------------
# 1️⃣ Clone the Repository
# -------------------------------
git clone <your-repo-url>
cd Kushagra_Gupta_Binance_Bot

# -------------------------------
# 2️⃣ Create & Activate Virtual Environment (Optional)
# -------------------------------
# Create virtual environment
python -m venv venv

# Activate virtual environment
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# -------------------------------
# 3️⃣ Create an .env File
# -------------------------------
# In the project root, create a file named .env and add your Binance API credentials:

# Content of .env
# API_KEY=YOUR_BINANCE_KEY
# API_SECRET=YOUR_BINANCE_SECRET

# ⚠️ Never push .env to GitHub

# -------------------------------
# ▶️ Run the Trading Bot
# -------------------------------
cd src
python chatbot.py

# Choose order type:
# market / limit / stop-limit / oco / twap / grid

# Example input:
# Order type: market
# Side: BUY
# Symbol: BTCUSDT
# Quantity: 0.001

# -------------------------------
# 📜 Logging
# -------------------------------
# All order attempts — successful and failed — are recorded in bot.log (stored in project root)
# Log entries include:
# - Full API responses
# - Executed trades
# - Failed order attempts
# - Error messages & exceptions




