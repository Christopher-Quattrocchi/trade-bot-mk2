import ccxt

def abort_all_positions(exchange):
    try:
        # Fetch open positions
        positions = exchange.fetch_positions()

        # Ensure positions is a list
        if not isinstance(positions, list):
            positions = [positions]

        # Close each open position
        for position in positions:
            if position['side'] == 'buy':
                order_side = 'sell'
            else:
                order_side = 'buy'

            symbol = position['symbol']
            amount = position['amount']

            # Create a market order to close the position
            order = exchange.create_order(
                symbol=symbol,
                type='market',
                side=order_side,
                amount=amount
            )

            print(f"Closed position: {order}")

    except Exception as e:
        print(f"Error closing positions: {e}")