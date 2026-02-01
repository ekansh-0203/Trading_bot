from binance import Client
from bot.logging_config import get_logger

logger = get_logger(__name__)

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def place_order(self, **kwargs):
        logger.info(f"Order Request: {kwargs}")
        response = self.client.futures_create_order(**kwargs)
        logger.info(f"Order Response: {response}")
        return response
