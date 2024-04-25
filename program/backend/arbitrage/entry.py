from func_bridge import bridge_tokens

def open_arbitrage_position(exchange_buy, exchange_sell, symbol, amount, buy_price, sell_price):
    try:
        # Place buy order on the buy exchange
        buy_order = exchange_buy.create_market_buy_order(symbol, amount)
        print(f"Buy order placed on {exchange_buy.name}: {buy_order}")

        # Bridge the tokens to the destination chain
        from_chain = exchange_buy.chain
        to_chain = exchange_sell.chain
        token = exchange_buy.market(symbol)['info']
        bridge_tokens(from_chain, to_chain, token, amount)

        # Place sell order on the sell exchange
        sell_order = exchange_sell.create_market_sell_order(symbol, amount)
        print(f"Sell order placed on {exchange_sell.name}: {sell_order}")

        return {
            "buy_order": buy_order,
            "sell_order": sell_order
        }

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

        position = open_arbitrage_position(buy_exchange, sell_exchange, symbol, amount, buy_price, sell_price)

        if position:
            positions.append(position)

    return positions