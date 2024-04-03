import ccxt

def open_arbitrage_position(exchange_buy, exchange_sell, symbol, amount, buy_price, sell_price):
    try:
        # Place a buy order on the exchange with the lower price
        buy_order = exchange_buy.create_limit_buy_order(symbol, amount, buy_price)
        print(f"Buy order placed on {exchange_buy.name}: {buy_order}")

        # Place a sell order on the exchange with the higher price
        sell_order = exchange_sell.create_limit_sell_order(symbol, amount, sell_price)
        print(f"Sell order placed on {exchange_sell.name}: {sell_order}")

        # Return the order details
        return {
            "buy_order": buy_order,
            "sell_order": sell_order
        }

    except ccxt.InsufficientFunds as e:
        print(f"Insufficient funds to open arbitrage position: {e}")
        return None

    except ccxt.InvalidOrder as e:
        print(f"Invalid order when opening arbitrage position: {e}")
        return None

    except Exception as e:
        print(f"Error opening arbitrage position: {e}")
        return None

def open_arbitrage_positions(exchanges, arbitrage_opportunities):
    positions = []

    for opportunity in arbitrage_opportunities:
        symbol = opportunity["symbol"]
        buy_exchange = exchanges[opportunity["buy_exchange"]]
        buy_price = opportunity["buy_price"]
        sell_exchange = exchanges[opportunity["sell_exchange"]]
        sell_price = opportunity["sell_price"]
        amount = opportunity["amount"]

        # Open the arbitrage position
        position = open_arbitrage_position(buy_exchange, sell_exchange, symbol, amount, buy_price, sell_price)

        if position:
            positions.append(position)

    return positions