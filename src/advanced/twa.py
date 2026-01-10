from market_orders import market_buy, market_sell
import time

def twap_order(symbol, side, total_qty, chunks=5, interval=30):
    """
    TWAP: split total_qty into smaller chunks over time
    """
    qty_per_order = total_qty / chunks
    for i in range(chunks):
        print(f"TWAP chunk {i+1}/{chunks}")
        if side.upper() == "BUY":
            market_buy(symbol, qty_per_order)
        else:
            market_sell(symbol, qty_per_order)
        time.sleep(interval)
