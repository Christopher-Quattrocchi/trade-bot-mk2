import ccxt
import pandas as pd

def fetch_market_prices(exchanges, symbol):
    prices = {}

    for exchange_name, exchange in exchanges.items():
        try:
            if exchange_name == "bitstamp":
                # Bitstamp uses a different symbol format
                symbol = symbol.replace("/", "").lower()
            elif exchange_name == "poloniex":
                # Poloniex uses a different symbol format
                symbol = symbol.replace("/", "_")
            
            ticker = exchange.fetch_ticker(symbol)
            # ...
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