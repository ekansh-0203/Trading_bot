from bot.validator import validate_order_inputs
from bot.logging_config import get_logger

logger = get_logger(__name__)

def create_order(client, symbol, side, order_type, quantity, price=None):
    validate_order_inputs(symbol, side, order_type, quantity, price)

    order_data = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        order_data["price"] = price
        order_data["timeInForce"] = "GTC"

    try:
        response = client.place_order(**order_data)
        return response
    except Exception as e:
        logger.error(f"Order failed: {e}")
        raise
