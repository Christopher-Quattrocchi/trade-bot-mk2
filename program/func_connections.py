from decouple import config
import ccxt

def connect_exchanges():
    # Dictionary to store the exchange instances
    exchanges = {}

    # List of exchange names you want to connect to
    exchange_names = ['binance', 'kucoin']  # Will add a lot more here

    for exchange_name in exchange_names:
        # Retrieve the API key, secret, and other required parameters from the environment variables
        api_key = config(f"{exchange_name.upper()}_API_KEY")
        api_secret = config(f"{exchange_name.upper()}_API_SECRET")
        # Add more parameters if required by the specific exchange

        try:
            # Initialize the exchange
            exchange_class = getattr(ccxt, exchange_name)
            exchange = exchange_class({
                'apiKey': api_key,
                'secret': api_secret,
                # Add more parameters if required by the specific exchange
            })

            # Load markets
            exchange.load_markets()

            # Add the exchange instance to the dictionary
            exchanges[exchange_name] = exchange

            print(f"Connection to {exchange_name} successful")
        except Exception as e:
            print(f"Error connecting to {exchange_name}: {e}")

    # Return the dictionary of exchange instances
    return exchanges