from client import get_client
import logging

client = get_client()

def oco_order(symbol, side, quantity, take_profit_price, stop_price, stop_limit_price):
    """
    Place OCO (take-profit + stop-loss) on Binance Futures Testnet
    """
    try:
        # Take profit order
        tp_order = client.futures_create_order(
            symbol=symbol,
            side="SELL" if side.upper() == "BUY" else "BUY",
            type="LIMIT",
            quantity=quantity,
            price=str(take_profit_price),
            timeInForce="GTC"
        )
        logging.info(f"OCO Take Profit ORDER: {tp_order}")

        # Stop-loss order
        sl_order = client.futures_create_order(
            symbol=symbol,
            side="SELL" if side.upper() == "BUY" else "BUY",
            type="STOP",
            quantity=quantity,
            stopPrice=str(stop_price),
            price=str(stop_limit_price),
            timeInForce="GTC"
        )
        logging.info(f"OCO Stop-Loss ORDER: {sl_order}")

        print("OCO orders placed (take-profit + stop-loss).")
        return tp_order, sl_order

    except Exception as e:
        logging.error(f"OCO FAILED: {e}")
        print("Error:", e)
