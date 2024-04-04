import ccxt
from func_bridge import bridge_tokens

def open_arbitrage_position(exchange_buy, exchange_sell, symbol, amount, buy_price, sell_price):
    try:
        if exchange_buy.id == "poloniex":
            # Poloniex requires a different order type
            buy_order = exchange_buy.create_limit_buy_order(symbol, amount, buy_price)
        else:
            buy_order = exchange_buy.create_market_buy_order(symbol, amount)

        print(f"Buy order placed on {exchange_buy.name}: {buy_order}")

        # Sell the token on the sell exchange
        sell_token(exchange_sell, symbol, amount)
        
        # Bridge the tokens to the target chain
        from_chain = exchange_sell.chain # assuming the exchange object has a chain attribute
        to_chain = exchange_buy.chain
        token = exchange_sell.market(symbol)['info']
        bridge_tokens(from_chain, to_chain, token, amount)

        return {
            "buy_order": buy_order,
            "sell_order": None  # Updated to None since sell_order is handled by sell_token
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

        position = open_arbitrage_position(buy_exchange, sell_exchange, symbol, amount, buy_price, sell_price)

        if position:
            positions.append(position)

    return positions

def sell_token(exchange, symbol, amount):
  try:
    # Fetch the token and exchange information
    market = exchange.market(symbol)
    token_address = market['info']['address']
    
    # Approve the router to spend the token
    approve_tx = exchange.approve({
      'token': token_address,
      'amount': amount,
    })
    print(f"Approval transaction: {approve_tx['info']['transactionHash']}")
    
    # Sell the token on the exchange
    sell_tx = exchange.create_market_sell_order(symbol, amount)
    print(f"Token sale successful. Transaction: {sell_tx}")
    
  except ccxt.InsufficientFunds as e:
    print(f"Insufficient funds to sell the token: {e}")
  except ccxt.InvalidOrder as e:
    print(f"Invalid Order: {e}")
  except Exception as e:
    print(f"Error selling the token: {e}")
    
