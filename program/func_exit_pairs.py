import ccxt
from func_bridge import bridge_tokens

def check_order_status(exchange, order_id):
    try:
        order = exchange.fetch_order(order_id)
        return order["status"]
    except Exception as e:
        print(f"Error checking order status: {e}")
        return None

def close_arbitrage_position(exchange, symbol, order_id):
    try:
        if exchange.id == "bittrex":
            # Bittrex requires a different method to cancel orders
            exchange.cancel_order(order_id, symbol)
        else:
            exchange.cancel_order(order_id)
            
        if exchange.chain != 'target_chain': # replace target chain with desired target chain
          token = exchange.market(symbol)['info']
          amount = exchange.fetch_order(order_id)['amount']
          bridge_tokens(exchange.chain, 'target_chain', token, amount)

        order_status = check_order_status(exchange, order_id)

        if order_status == "closed":
            print(f"Order {order_id} on {exchange.name} is already closed.")
            return True
        elif order_status == "canceled":
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
        buy_exchange = exchanges[trade["buy_exchange"]]
        buy_order_id = trade["buy_order"]["id"]
        sell_exchange = exchanges[trade["sell_exchange"]]
        sell_order_id = trade["sell_order"]["id"]

        buy_closed = close_arbitrage_position(buy_exchange, trade["symbol"], buy_order_id)
        sell_closed = close_arbitrage_position(sell_exchange, trade["symbol"], sell_order_id)

        if buy_closed and sell_closed:
            closed_trades.append(trade)

    return closed_trades