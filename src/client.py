import os
from dotenv import load_dotenv
from binance.client import Client

# Load environment variables from .env file
load_dotenv()

# Fetch key & secret
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")

def get_client():
    """
    Returns a Binance Futures Testnet client instance.
    """
    if not API_KEY or not API_SECRET:
        raise Exception("API credentials missing! Add BINANCE_API_KEY and BINANCE_SECRET_KEY to your .env file.")

    client = Client(API_KEY, API_SECRET)

    # Change REST endpoint to Binance Futures TESTNET
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    
    return client
