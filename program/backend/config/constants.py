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


## THIS STUFF IS FOR TRYING TO INTEGRATE STARGATE!! ##
# Layer zero endpoint/id

# Ethereum Mainnet
ETHEREUM_ENDPOINT = "0x1a44076050125825900e736c501f859c50fe728c"
ETHEREUM_ENDPOINT_ID = "30101"

# BNB Chain (Binance Smart Chain)
BNBCHAIN_ENDPOINT = "0x1a44076050125825900e736c501f859c50fe728c"
BNBCHAIN_ENDPOINT_ID = "30102"

# Avalanche
AVALANCHE_ENDPOINT = "0x1a44076050125825900e736c501f859c50fe728c"
AVALANCHE_ENDPOINT_ID = "30106"

# Polygon
POLYGON_ENDPOINT = "0x1a44076050125825900e736c501f859c50fe728c"
POLYGON_ENDPOINT_ID = "30109"

# Arbitrum
ARBITRUM_ENDPOINT = "0x1a44076050125825900e736c501f859c50fe728c"
ARBITRUM_ENDPOINT_ID = "30110"

# Optimism
OPTIMISM_ENDPOINT = "0x1a44076050125825900e736c501f859c50fe728c"
OPTIMISM_ENDPOINT_ID = "30111"

# Fantom
FANTOM_ENDPOINT = "0x1a44076050125825900e736c501f859c50fe728c"
FANTOM_ENDPOINT_ID = "30112"

# Stargate Mainnet Contract Addresses
STARGATE_CONTRACTS = {
    "Ethereum": {
        "chainId": "101",
        "Router": "0x8731d54E9D02c286767d56ac03e8037C07e01e98",
        "RouterETH": "0x150f94B44927F078737562f0fcF3C95c01Cc2376",
        "Bridge": "0x296F55F8Fb28E498B858d0BcDA06D955B2Cb3f97",
        "Factory": "0x06D538690AF257Da524f25D0CD52fD85b1c2173E",
        "StargateToken": "0xAf5191B0De278C7286d6C7CC6ab6BB8A73bA2Cd6",
        "FeeLibrary": "0x8C3085D9a554884124C998CDB7f6d7219E9C1e6F",
        "Composer": "0xeCc19E177d24551aA7ed6Bc6FE566eCa726CC8a9",
        "WidgetSwap": "0x10d16248bED1E0D0c7cF94fFD99A50c336c7Bcdc"
    },
    "BNB_Chain": {
        "chainId": "102",
        "Router": "0x4a364f8c717cAAD9A442737Eb7b8A55cc6cf18D8",
        "Bridge": "0x6694340fc020c5E6B96567843da2df01b2CE1eb6",
        "Factory": "0xe7Ec689f432f29383f217e36e680B5C855051f25",
        "StargateToken": "0xB0D502E938ed5f4df2E681fE6E419ff29631d62b",
        "FeeLibrary": "0xCA6522116e8611A346D53Cc2005AC4192e3fc2BC",
        "Composer": "0xeCc19E177d24551aA7ed6Bc6FE566eCa726CC8a9",
        "WidgetSwap": "0x10d16248bED1E0D0c7cF94fFD99A50c336c7Bcdc"
    },
    "Avalanche": {
        "chainId": "106",
        "Router": "0x45A01E4e04F14f7A4a6702c74187c5F6222033cd",
        "Bridge": "0x9d1B1669c73b033DFe47ae5a0164Ab96df25B944",
        "Factory": "0x808d7c71ad2ba3FA531b068a2417C63106BC0949",
        "StargateToken": "0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590",
        "FeeLibrary": "0x5E8eC15ACB5Aa94D5f0589E54441b31c5e0B992d",
        "Composer": "0xeCc19E177d24551aA7ed6Bc6FE566eCa726CC8a9",
        "WidgetSwap": "0x10d16248bED1E0D0c7cF94fFD99A50c336c7Bcdc"
    },
    "Polygon": {
        "chainId": "109",
        "Router": "0x45A01E4e04F14f7A4a6702c74187c5F6222033cd",
        "Bridge": "0x9d1B1669c73b033DFe47ae5a0164Ab96df25B944",
        "Factory": "0x808d7c71ad2ba3FA531b068a2417C63106BC0949",
        "StargateToken": "0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590",
        "FeeLibrary": "0xb279b324Ea5648bE6402ABc727173A225383494C",
        "Composer": "0xeCc19E177d24551aA7ed6Bc6FE566eCa726CC8a9",
        "WidgetSwap": "0x10d16248bED1E0D0c7cF94fFD99A50c336c7Bcdc"
    },
    "Arbitrum": {
        "chainId": "110",
        "Router": "0x53Bf833A5d6c4ddA888F69c22C88C9f356a41614",
        "RouterETH": "0xbf22f0f184bCcbeA268dF387a49fF5238dD23E40",
        "Bridge": "0x352d8275AAE3e0c2404d9f68f6cEE084B5bEB3DD",
        "Factory": "0x55bDb4164D28FBaF0898e0eF14a589ac09Ac9970",
        "StargateToken": "0x6694340fc020c5E6B96567843da2df01b2CE1eb6",
        "FeeLibrary": "0x1cF31666c06ac3401ed0C1c6346C4A9425dd7De4",
        "Composer": "0xeCc19E177d24551aA7ed6Bc6FE566eCa726CC8a9",
        "WidgetSwap": "0x10d16248bED1E0D0c7cF94fFD99A50c336c7Bcdc"
    },
    "Optimism": {
        "chainId": "111",
        "Router": "0xB0D502E938ed5f4df2E681fE6E419ff29631d62b",
        "RouterETH": "0xB49c4e680174E331CB0A7fF3Ab58afC9738d5F8b",
        "Bridge": "0x701a95707A0290AC8B90b3719e8EE5b210360883",
        "Factory": "0xE3B53AF74a4BF62Ae5511055290838050bf764Df",
        "StargateToken": "0x296F55F8Fb28E498B858d0BcDA06D955B2Cb3f97",
        "FeeLibrary": "0x505eCDF2f14Cd4f1f413d04624b009A449D38D7E",
        "Composer": "0xeCc19E177d24551aA7ed6Bc6FE566eCa726CC8a9",
        "WidgetSwap": "0x10d16248bED1E0D0c7cF94fFD99A50c336c7Bcdc"
    },
    "Fantom": {
        "chainId": "112",
        "Router": "0xAf5191B0De278C7286d6C7CC6ab6BB8A73bA2Cd6",
        "Bridge": "0x45A01E4e04F14f7A4a6702c74187c5F6222033cd",
        "Factory": "0x9d1B1669c73b033DFe47ae5a0164Ab96df25B944",
        "StargateToken": "0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590",
        "FeeLibrary": "0x616a68BD6DAd19e066661C7278611487d4072839",
        "Composer": "0xeCc19E177d24551aA7ed6Bc6FE566eCa726CC8a9",
        "WidgetSwap": "0x10d16248bED1E0D0c7cF94fFD99A50c336c7Bcdc"
    },
    "Base": {
        "chainId": "184",
        "Router": "0x45f1A95A4D3f3836523F5c83673c797f4d4d263B",
        "RouterETH": "0x50B6EbC2103BFEc165949CC946d739d5650d7ae4",
        "Bridge": "0xAF54BE5B6eEc24d6BFACf1cce4eaF680A8239398",
        "Factory": "0xAf5191B0De278C7286d6C7CC6ab6BB8A73bA2Cd6",
        "StargateToken": "0xE3B53AF74a4BF62Ae5511055290838050bf764Df",
        "FeeLibrary": "0x9d1b1669c73b033dfe47ae5a0164ab96df25b944",
        "Composer": "0xeCc19E177d24551aA7ed6Bc6FE566eCa726CC8a9",
        "WidgetSwap": "0x10d16248bED1E0D0c7cF94fFD99A50c336c7Bcdc",
        "PoolETH": "0x28fc411f9e1c480AD312b3d9C60c22b965015c6B",
        "PoolUSDC": "0x4c80E24119CFB836cdF0a6b53dc23F04F7e652CA",
        "LPStaking": "0x06Eb48763f117c7Be887296CDcdfad2E4092739C"
    },
    "Linea": {
        "chainId": "183",
        "Router": "0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590",
        "RouterETH": "0x8731d54E9D02c286767d56ac03e8037C07e01e98",
        "Bridge": "0x45f1A95A4D3f3836523F5c83673c797f4d4d263B",
        "Factory": "0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398",
        "StargateToken": "0x808d7c71ad2ba3FA531b068a2417C63106BC0949",
        "FeeLibrary": "0x45A01E4e04F14f7A4a6702c74187c5F6222033cd",
        "Composer": "0xeCc19E177d24551aA7ed6Bc6FE566eCa726CC8a9",
        "WidgetSwap": "0x10d16248bED1E0D0c7cF94fFD99A50c336c7Bcdc",
        "PoolETH": "0xAad094F6A75A14417d39f04E690fC216f080A41a",
        "LPStaking": "0x4a364f8c717cAAD9A442737Eb7b8A55cc6cf18D8"
    },
    "Kava": {
        "chainId": "177",
        "Router": "0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590",
        "Bridge": "0x45f1A95A4D3f3836523F5c83673c797f4d4d263B",
        "Factory": "0xAF54BE5B6eEc24d6BFACf1cce4eaF680A8239398",
        "StargateToken": "0x83c30eb8bc9ad7C56532895840039E62659896ea",
        "FeeLibrary": "0x45a01e4e04f14f7a4a6702c74187c5f6222033cd",
        "Composer": "0xeCc19E177d24551aA7ed6Bc6FE566eCa726CC8a9",
        "WidgetSwap": "0x10d16248bED1E0D0c7cF94fFD99A50c336c7Bcdc"
    },
    "Mantle": {
        "chainId": "181",
        "Router": "0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590",
        "Bridge": "0x45f1A95A4D3f3836523F5c83673c797f4d4d263B",
        "Factory": "0xAF54BE5B6eEc24d6BFACf1cce4eaF680A8239398",
        "StargateToken": "0x8731d54E9D02c286767d56ac03e8037C07e01e98",
        "FeeLibrary": "0x45A01E4e04F14f7A4a6702c74187c5F6222033cd",
        "Composer": "0x296F55F8Fb28E498B858d0BcDA06D955B2Cb3f97",
        "WidgetSwap": "0x06D538690AF257Da524f25D0CD52fD85b1c2173E"
    }
}