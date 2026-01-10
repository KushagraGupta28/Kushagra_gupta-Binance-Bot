def grid_orders(symbol, side, start_price, end_price, levels=5, qty_per_order=0.002):
    """
    Place a grid of limit orders between start_price and end_price
    """
    grid_prices = [round(start_price + i * (end_price - start_price)/(levels-1), 2) for i in range(levels)]
    
    for price in grid_prices:
        if side.upper() == "BUY":
            limit_buy(symbol, qty_per_order, price)
        else:
            limit_sell(symbol, qty_per_order, price)
        print(f"Grid {side} order at {price} placed.")
