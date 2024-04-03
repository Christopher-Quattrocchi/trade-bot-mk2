def check_order_status(exchange, order_id):
    try:
        order = exchange.fetch_order(order_id)
        return order['status']
    except Exception as e:
        print(f"Error checking order status: {e}")
        return None

def close_arbitrage_position(exchange, symbol, order_id):
    try:
        order_status = check_order_status(exchange, order_id)

        if order_status == 'closed':
            print(f"Order {order_id} on {exchange.name} is already closed.")
            return True
        elif order_status == 'open':
            # Cancel the open order
            exchange.cancel_order(order_id)
            print(f"Order {order_id} on {exchange.name} has been canceled.")
            return True
        else:
            print(f"Order {order_id} on {exchange.name} has an unexpected status: {order_status}")
            return False

    except Exception as e:
        print(f"Error closing arbitrage position: {e}")
        return False

def manage_arbitrage_exits(exchanges, successful_trades):
    closed_trades = []

    for trade in successful_trades:
        buy_exchange = exchanges[trade['buy_exchange']]
        buy_order_id = trade['buy_order_id']
        sell_exchange = exchanges[trade['sell_exchange']]
        sell_order_id = trade['sell_order_id']

        # Close the buy position
        buy_closed = close_arbitrage_position(buy_exchange, trade['symbol'], buy_order_id)

        # Close the sell position
        sell_closed = close_arbitrage_position(sell_exchange, trade['symbol'], sell_order_id)

        if buy_closed and sell_closed:
            closed_trades.append(trade)

    return closed_trades