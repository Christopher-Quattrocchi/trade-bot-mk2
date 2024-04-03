from func_connections import connect_exchanges
from func_public import construct_market_prices
from func_arbitrage import find_arbitrage_opportunities
from func_entry_pairs import open_arbitrage_positions
from func_exit_pairs import manage_arbitrage_exits

# Define the list of trading pairs to monitor
symbols = ['BTC/USDT', 'ETH/USDT', 'XRP/USDT']

# Define the minimum profit percentage threshold
min_profit_percentage = 1.0

# Define the maximum exposure per trade
max_exposure = 1000

def main():
    # Connect to the exchanges
    exchanges = connect_exchanges()

    while True:
        try:
            # Fetch market prices from exchanges
            market_prices = construct_market_prices(exchanges, symbols)

            # Identify arbitrage opportunities
            arbitrage_opportunities = find_arbitrage_opportunities(market_prices, min_profit_percentage)

            # Print the identified arbitrage opportunities
            print(f"Found {len(arbitrage_opportunities)} arbitrage opportunities:")
            for opportunity in arbitrage_opportunities:
                print(opportunity)

            # Open arbitrage positions
            successful_trades = open_arbitrage_positions(exchanges, arbitrage_opportunities, max_exposure)

            # Manage arbitrage position exits
            closed_trades = manage_arbitrage_exits(exchanges, successful_trades)

            # Print the closed trades
            print(f"Closed {len(closed_trades)} arbitrage positions:")
            for trade in closed_trades:
                print(trade)

        except KeyboardInterrupt:
            print("Bot interrupted by user. Exiting...")
            break

        except Exception as e:
            print(f"Error in main loop: {e}")

if __name__ == '__main__':
    main()