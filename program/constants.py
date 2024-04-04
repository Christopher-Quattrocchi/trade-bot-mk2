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

#Rabby Private Key
RABBY_PRIVATE_KEY = config("RABBY_PRIVATE_KEY")

# Exchange API Keys
BINANCE_API_KEY = config("BINANCE_API_KEY")
BINANCE_API_SECRET = config("BINANCE_API_SECRET")
COINBASE_PRO_API_KEY = config("COINBASE_PRO_API_KEY")
COINBASE_PRO_API_SECRET = config("COINBASE_PRO_API_SECRET")
COINBASE_PRO_API_PASSPHRASE = config("COINBASE_PRO_API_PASSPHRASE")
KRAKEN_API_KEY = config("KRAKEN_API_KEY")
KRAKEN_API_SECRET = config("KRAKEN_API_SECRET")
BITFINEX_API_KEY = config("BITFINEX_API_KEY")
BITFINEX_API_SECRET = config("BITFINEX_API_SECRET")
HUOBI_API_KEY = config("HUOBI_API_KEY")
HUOBI_API_SECRET = config("HUOBI_API_SECRET")
OKEX_API_KEY = config("OKEX_API_KEY")
OKEX_API_SECRET = config("OKEX_API_SECRET")
OKEX_API_PASSPHRASE = config("OKEX_API_PASSPHRASE")
KUCOIN_API_KEY = config("KUCOIN_API_KEY")
KUCOIN_API_SECRET = config("KUCOIN_API_SECRET")
KUCOIN_API_PASSPHRASE = config("KUCOIN_API_PASSPHRASE")
BITSTAMP_API_KEY = config("BITSTAMP_API_KEY")
BITSTAMP_API_SECRET = config("BITSTAMP_API_SECRET")
BITTREX_API_KEY = config("BITTREX_API_KEY")
BITTREX_API_SECRET = config("BITTREX_API_SECRET")
POLONIEX_API_KEY = config("POLONIEX_API_KEY")
POLONIEX_API_SECRET = config("POLONIEX_API_SECRET")
GATEIO_API_KEY = config("GATEIO_API_KEY")
GATEIO_API_SECRET = config("GATEIO_API_SECRET")

# Exchange Instances
EXCHANGE_BINANCE = ccxt.binance({
    "apiKey": BINANCE_API_KEY,
    "secret": BINANCE_API_SECRET
})

EXCHANGE_COINBASE_PRO = ccxt.coinbasepro({
    "apiKey": COINBASE_PRO_API_KEY,
    "secret": COINBASE_PRO_API_SECRET,
    "password": COINBASE_PRO_API_PASSPHRASE
})

EXCHANGE_KRAKEN = ccxt.kraken({
    "apiKey": KRAKEN_API_KEY,
    "secret": KRAKEN_API_SECRET
})

EXCHANGE_BITFINEX = ccxt.bitfinex({
    "apiKey": BITFINEX_API_KEY,
    "secret": BITFINEX_API_SECRET
})

EXCHANGE_HUOBI = ccxt.huobipro({
    "apiKey": HUOBI_API_KEY,
    "secret": HUOBI_API_SECRET
})

EXCHANGE_OKEX = ccxt.okex({
    "apiKey": OKEX_API_KEY,
    "secret": OKEX_API_SECRET,
    "password": OKEX_API_PASSPHRASE
})

EXCHANGE_KUCOIN = ccxt.kucoin({
    "apiKey": KUCOIN_API_KEY,
    "secret": KUCOIN_API_SECRET,
    "password": KUCOIN_API_PASSPHRASE
})

EXCHANGE_BITSTAMP = ccxt.bitstamp({
    "apiKey": BITSTAMP_API_KEY,
    "secret": BITSTAMP_API_SECRET
})

EXCHANGE_BITTREX = ccxt.bittrex({
    "apiKey": BITTREX_API_KEY,
    "secret": BITTREX_API_SECRET
})

EXCHANGE_POLONIEX = ccxt.poloniex({
    "apiKey": POLONIEX_API_KEY,
    "secret": POLONIEX_API_SECRET
})

EXCHANGE_GATEIO = ccxt.gateio({
    "apiKey": GATEIO_API_KEY,
    "secret": GATEIO_API_SECRET
})

## Supported Exchanges
EXCHANGES = {
    "binance": EXCHANGE_BINANCE,
    "coinbasepro": EXCHANGE_COINBASE_PRO,
    "kraken": EXCHANGE_KRAKEN,
    "bitfinex": EXCHANGE_BITFINEX,
    "huobi": EXCHANGE_HUOBI,
    "okex": EXCHANGE_OKEX,
    "kucoin": EXCHANGE_KUCOIN,
    "bitstamp": EXCHANGE_BITSTAMP,
    "bittrex": EXCHANGE_BITTREX,
    "poloniex": EXCHANGE_POLONIEX,
    "gateio": EXCHANGE_GATEIO
}

# Supported Trading Pairs
TRADING_PAIRS = ["BTC/USDT", "ETH/USDT", "XRP/USDT"]