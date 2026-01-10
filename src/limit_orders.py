import logging
from client import get_client

client = get_client()

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------------------
# Helpers
# -----------------------------------------
def get_tick_size(symbol):
    info = client.futures_exchange_info()
    for s in info['symbols']:
        if s['symbol'] == symbol:
            for f in s['filters']:
                if f['filterType'] == 'PRICE_FILTER':
                    return float(f['tickSize'])
    return 0.01  # fallback

def round_tick(price, tick):
    return round(price / tick) * tick

# -----------------------------------------
# LIMIT ORDERS
# -----------------------------------------
def limit_buy(symbol="BTCUSDT", qty=0.002, price=None):
    tick = get_tick_size(symbol)
    price = round_tick(price, tick)

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side="BUY",
            type="LIMIT",
            timeInForce="GTC",
            quantity=qty,
            price=str(price)
        )
        logging.info(f"LIMIT BUY {symbol} qty={qty}@{price} SUCCESS {order}")
        print("LIMIT BUY SUCCESS:", order)
        return order
    except Exception as e:
        logging.error(f"LIMIT BUY FAILED: {e}")
        print("Error:", e)

def limit_sell(symbol="BTCUSDT", qty=0.002, price=None):
    tick = get_tick_size(symbol)
    price = round_tick(price, tick)

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side="SELL",
            type="LIMIT",
            timeInForce="GTC",
            quantity=qty,
            price=str(price)
        )
        logging.info(f"LIMIT SELL {symbol} qty={qty}@{price} SUCCESS {order}")
        print("LIMIT SELL SUCCESS:", order)
        return order
    except Exception as e:
        logging.error(f"LIMIT SELL FAILED: {e}")
        print("Error:", e)

# -----------------------------------------
# NEW: STOP-LIMIT ORDER
# -----------------------------------------
def stop_limit_order(symbol="BTCUSDT", side="BUY", qty=0.002, stop_price=None, limit_price=None):
    tick = get_tick_size(symbol)
    stop_price = round_tick(stop_price, tick)
    limit_price = round_tick(limit_price, tick)

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="STOP",
            timeInForce="GTC",
            quantity=qty,
            stopPrice=str(stop_price),
            price=str(limit_price)
        )
        logging.info(f"STOP LIMIT {side} {symbol} qty={qty} stop={stop_price} limit={limit_price} SUCCESS {order}")
        print(f"STOP LIMIT {side} SUCCESS:", order)
        return order
    except Exception as e:
        logging.error(f"STOP LIMIT {side} FAILED: {e}")
        print("Error:", e)

# -----------------------------------------
# Quick test
# -----------------------------------------
if __name__ == "__main__":
    symbol = "BTCUSDT"
    price = float(client.futures_symbol_ticker(symbol=symbol)['price'])

    limit_buy(symbol, 0.002, price * 0.99)
    limit_sell(symbol, 0.002, price * 1.01)
    stop_limit_order(symbol, "BUY", 0.002, price * 1.005, price * 1.01)
