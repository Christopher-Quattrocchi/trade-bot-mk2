import ccxt
import pandas as pd

def fetch_market_prices(exchanges, symbol):
    prices = {}

    for exchange_name, exchange in exchanges.items():
        try:
            # Fetch the ticker for the specified symbol
            ticker = exchange.fetch_ticker(symbol)

            # Extract the last price from the ticker
            last_price = ticker['last']

            # Store the price in the dictionary
            prices[exchange_name] = last_price

        except Exception as e:
            print(f"Error fetching price from {exchange_name}: {e}")

    return prices

def construct_market_prices(exchanges, symbols):
    market_prices = {}

    for symbol in symbols:
        prices = fetch_market_prices(exchanges, symbol)
        market_prices[symbol] = prices

    # Create a DataFrame from the market prices
    df_market_prices = pd.DataFrame.from_dict(market_prices)

    return df_market_prices