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

/Kushagra_Gupta_Binance_Bot/
│
├── .env # Stores API key + secret (DO NOT COMMIT)
├── bot.log # Log file saving both successful and failed orders
├── README.md # You are reading it :)
│
├── /src/
│ ├── chatbot.py # CLI that takes interactive user input
│ ├── client.py # Authenticated Binance client
│ ├── market_orders.py # Market buy/sell functions
│ ├── limit_orders.py # Limit + Stop-Limit functions
│ │
│ ├── /advanced/
│ │ ├── oco.py # OCO dual-leg order handler
│ │ ├── twa.py # TWAP execution engine
│ │ └── ga.py # Grid strategy execution
│ │
│ └── pycache/ # Auto-generated cache
│
└── venv/ (optional)


