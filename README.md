🚀 Binance Futures Trading Bot

A Python-based interactive CLI bot that executes Binance USDT-M Futures orders in real time.
Supports Market Orders, Limit Orders and advanced strategies like Stop-Limit, OCO, TWAP, and Grid trading.

📦 Features Implemented
🔹 Core Order Types

✔ Market Buy/Sell
✔ Limit Buy/Sell
✔ Stop-Limit Orders (included inside limit_orders.py)

🔹 Advanced Order Systems (Bonus)

✔ OCO Orders (One Cancels the Other)
✔ TWAP (Time-Weighted Average Price execution)
✔ Grid Strategy (Auto buy-low / sell-high across levels)

🧱 Project Structure
/Kushagra_Gupta_Binance_Bot/
│
├── .env                       # Stores API key + secret (DO NOT COMMIT)
├── bot.log                    # Log file saving both successful and failed orders
├── README.md                  # You are reading it :)
│
├── /src/
│   ├── chatbot.py             # CLI that takes interactive user input
│   ├── client.py              # Authenticated Binance client
│   ├── market_orders.py       # Market buy/sell functions
│   ├── limit_orders.py        # Limit + Stop-Limit functions
│   │
│   ├── /advanced/
│   │   ├── oco.py             # OCO Dual-Leg order handler
│   │   ├── twa.py             # TWAP execution engine
│   │   └── ga.py              # Grid strategy execution
│   │
│   └── __pycache__            # Auto-generated cache
│
└── venv/ (optional)

🔧 Installation & Setup
1️⃣ Clone the repo
git clone <your-repo-url>
cd Kushagra_Gupta_Binance_Bot

2️⃣ Create & Activate Virtual Environment (optional)
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3️⃣ Create an .env File

📁 In the project root, create a file named .env and add:

API_KEY=YOUR_BINANCE_KEY
API_SECRET=YOUR_BINANCE_SECRET


⚠️ Never push .env to GitHub

▶️ Run the Trading Bot
cd src
python chatbot.py


Follow prompts to choose:

market / limit / stop-limit / oco / twap / grid


Example:

Order type: market
Side: BUY
Symbol: BTCUSDT
Quantity: 0.001

📜 Logging

All order attempts — successful or failed — are written to:

bot.log (stored in project root)

This includes errors, fills, rejections, and API responses.


🙌 Credits / Author

Kushagra Gupta
Built as part of assignment evaluation for
Junior Python Developer – Crypto Trading Bot
