def find_arbitrage_opportunities(market_prices, min_profit_percentage):
    opportunities = []

    for symbol, prices in market_prices.items():
        max_price = max(prices.values())
        min_price = min(prices.values())

        # Calculate the potential profit percentage
        profit_percentage = (max_price - min_price) / min_price * 100

        if profit_percentage >= min_profit_percentage:
            opportunity = {
                'symbol': symbol,
                'buy_exchange': min(prices, key=prices.get),
                'buy_price': min_price,
                'sell_exchange': max(prices, key=prices.get),
                'sell_price': max_price,
                'profit_percentage': profit_percentage
            }
            opportunities.append(opportunity)

    return opportunities