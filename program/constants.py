import ccxt
from decouple import config

# !!! SELECT MODE !!!!!
MODE = "DEVELOPMENT"

# Close all open positions and orders
ABORT_ALL_POSITIONS = False

# Place Trades
PLACE_TRADES = True

# Thresholds - Opening
MIN_PROFIT_PERCENTAGE = 1.0  # Minimum profit percentage threshold

# Thresholds - Closing
CLOSE_AT_PROFIT_THRESHOLD = True

# Exchange API Keys
BINANCE_API_KEY = config("BINANCE_API_KEY")
BINANCE_API_SECRET = config("BINANCE_API_SECRET")
KUCOIN_API_KEY = config("KUCOIN_API_KEY")
KUCOIN_API_SECRET = config("KUCOIN_API_SECRET")
KUCOIN_API_PASSPHRASE = config("KUCOIN_API_PASSPHRASE")

# Exchange Instances
EXCHANGE_BINANCE = ccxt.binance({
    "apiKey": BINANCE_API_KEY,
    "secret": BINANCE_API_SECRET
})

EXCHANGE_KUCOIN = ccxt.kucoin({
    "apiKey": KUCOIN_API_KEY,
    "secret": KUCOIN_API_SECRET,
    "password": KUCOIN_API_PASSPHRASE
})

# Supported Exchanges
EXCHANGES = {
    "binance": EXCHANGE_BINANCE,
    "kucoin": EXCHANGE_KUCOIN
}

# Supported Trading Pairs
TRADING_PAIRS = ["BTC/USDT", "ETH/USDT", "XRP/USDT"]