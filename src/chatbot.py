from market_orders import market_buy, market_sell
from limit_orders import limit_buy, limit_sell , stop_limit_order
from advanced.oco import oco_order
from advanced.twa import twap_order
from advanced.ga import grid_orders  
from client import get_client
import logging
# Initialize client
import os
client = get_client()

# Setup logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_DIR, "bot.log")

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Get list of valid futures symbols
valid_symbols = [s['symbol'] for s in client.futures_exchange_info()['symbols']]

# -------------------------
# Validation helpers
# -------------------------
def validate_symbol(symbol):
    if symbol not in valid_symbols:
        raise ValueError(f"Symbol {symbol} is invalid. Choose from: {', '.join(valid_symbols[:5])} ...")
    return symbol

def validate_side(side):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side

def validate_order_type(order_type):
    order_type = order_type.lower()
    allowed = ["market", "limit", "stop-limit", "oco", "twap", "grid"]
    if order_type not in allowed:
        raise ValueError(f"Order type must be one of: {', '.join(allowed)}")
    return order_type

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# -------------------------
# Interactive CLI Loop
# -------------------------
def main():
    print("=== Binance Futures Bot CLI ===")
    while True:
        try:
            order_type = input("\nOrder type (market/limit/stop-limit/oco/twap/grid, q to quit): ").strip().lower()
            if order_type == "q":
                print("Exiting...")
                break

            order_type = validate_order_type(order_type)

            if order_type in ["market", "limit", "stop-limit", "oco", "twap", "grid"]:
                side = validate_side(input("Side (BUY/SELL): ").strip())
                symbol = validate_symbol(input("Symbol (BTCUSDT, ETHUSDT, ...): ").strip().upper())

            # -------------------------
            # Handle each order type
            # -------------------------
            if order_type == "market":
                qty = get_float_input("Quantity: ")
                if side == "BUY":
                    market_buy(symbol, qty)
                else:
                    market_sell(symbol, qty)

            elif order_type == "limit":
                qty = get_float_input("Quantity: ")
                price = get_float_input("Limit price: ")
                if side == "BUY":
                    limit_buy(symbol, qty, price)
                else:
                    limit_sell(symbol, qty, price)

            elif order_type == "stop-limit":
                qty = get_float_input("Quantity: ")
                stop_price = get_float_input("Stop price: ")
                limit_price = get_float_input("Limit price: ")
                stop_limit_order(symbol, side, qty, stop_price, limit_price)

            elif order_type == "oco":
                qty = get_float_input("Quantity: ")
                take_profit = get_float_input("Take-profit price: ")
                stop_price = get_float_input("Stop-loss price: ")
                stop_limit_price = get_float_input("Stop-limit price (trigger for stop-loss): ")
                oco_order(symbol, side, qty, take_profit, stop_price, stop_limit_price)

            elif order_type == "twap":
                total_qty = get_float_input("Total quantity: ")
                chunks = int(get_float_input("Number of chunks: "))
                interval = int(get_float_input("Interval in seconds between orders: "))
                twap_order(symbol, side, total_qty, chunks, interval)

            elif order_type == "grid":
                qty = get_float_input("Quantity per order: ")
                start_price = get_float_input("Start price: ")
                end_price = get_float_input("End price: ")
                levels = int(get_float_input("Number of levels: "))
                grid_orders(symbol, side, start_price, end_price, levels, qty)

        except Exception as e:
            print("Error:", e)
            logging.error(f"User input error: {e}")

if __name__ == "__main__":
    main()
