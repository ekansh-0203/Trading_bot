import argparse
import os
from bot.client import BinanceFuturesClient
from bot.order import create_order
from bot.logging_config import get_logger

logger = get_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Future trading bot:")
    parser.add_argument("symbol:", required=True)
    parser.add_argument("side:", required=True)
    parser.add_argument("type:", required=True)
    parser.add_argument("quantity:", type=float, required=True)
    parser.add_argument("price:", type=float)

    args = parser.parse_args()

    api_key = os.getenv("9u6K7gFZzM0Zs8GkZ0WfXy7s8Rr4Z6gD")
    api_secret = os.getenv("1A2B3C4D5E6F7G8H9I0J")

    if not api_key or not api_secret:
        raise EnvironmentError("API credentials")

    client = BinanceFuturesClient(api_key, api_secret)

    print("\nOrder Summary")
    print(f"Symbol   : {args.symbol}")
    print(f"Side     : {args.side}")
    print(f"Type     : {args.type}")
    print(f"Quantity : {args.quantity}")
    print(f"Price    : {args.price}\n")

    try:
        order = create_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("Order Placed Successfully")
        print(f"Order ID     : {order['orderId']}")
        print(f"Status       : {order['status']}")
        print(f"Executed Qty : {order['executedQty']}")
        print(f"Avg Price    : {order.get('avgPrice', 'N/A')}")

    except Exception as e:
        print("Order Failed")
        print(str(e))

if __name__ == "__main__":
    main()
