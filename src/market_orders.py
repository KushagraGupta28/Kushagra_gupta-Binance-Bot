import os
import logging
from dotenv import load_dotenv
from client import get_client

# Load environment variables
load_dotenv()

# Setup logging to bot.log (project root)
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create client from your factory function
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")
client = get_client()

def market_buy(symbol="BTCUSDT", qty=0.001):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side="BUY",
            type="MARKET",
            quantity=qty
        )
        logging.info(f"Market BUY {symbol} qty={qty} → SUCCESS: {order}")
        print("Market BUY SUCCESS:", order)
        return order
    except Exception as e:
        logging.error(f"Market BUY FAILED: {e}")
        print("Error:", e)


def market_sell(symbol="BTCUSDT", qty=0.001):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side="SELL",
            type="MARKET",
            quantity=qty
        )
        logging.info(f"Market SELL {symbol} qty={qty} → SUCCESS: {order}")
        print("Market SELL SUCCESS:", order)
        return order
    except Exception as e:
        logging.error(f"Market SELL FAILED: {e}")
        print("Error:", e)


if __name__ == "__main__":
    market_buy("BTCUSDT", 0.003)
    market_sell("BTCUSDT", 0.003)
