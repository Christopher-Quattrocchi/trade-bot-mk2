#Probably don't want this anymore - Behavior should be explicitly user directed
def find_arbitrage_opportunities(market_prices, min_profit_percentage):
    opportunities = []

    for symbol, prices in market_prices.items():
        max_price = float("-inf")
        min_price = float("inf")
        max_exchange = None
        min_exchange = None

        for exchange_name, price in prices.items():
            if exchange_name == "gateio":
                # Gate.io has a different fee structure
                fee = 0.002  # Example fee, adjust as needed
            elif exchange_name == "poloniex":
                # Poloniex has a different fee structure
                fee = 0.0025  # Example fee, adjust as needed
            else:
                fee = 0.001  # Default fee for other exchanges

            # Adjust the price based on the exchange's fee
            adjusted_price = price * (1 - fee)

            if adjusted_price > max_price:
                max_price = adjusted_price
                max_exchange = exchange_name
            if adjusted_price < min_price:
                min_price = adjusted_price
                min_exchange = exchange_name

        # Calculate the potential profit percentage
        if min_price > 0:
            profit_percentage = ((max_price - min_price) / min_price) * 100
        else:
            continue

        if profit_percentage >= min_profit_percentage:
            # Calculate the trade amounts based on the available balances
            max_exchange_balance = market_prices[symbol][max_exchange]["balance"]
            min_exchange_balance = market_prices[symbol][min_exchange]["balance"]

            buy_amount = min(max_exchange_balance, min_exchange_balance)
            sell_amount = buy_amount

            opportunity = {
                "symbol": symbol,
                "buy_exchange": min_exchange,
                "buy_price": min_price,
                "sell_exchange": max_exchange,
                "sell_price": max_price,
                "amount": buy_amount,
                "profit_percentage": profit_percentage
            }
            opportunities.append(opportunity)

    return opportunities