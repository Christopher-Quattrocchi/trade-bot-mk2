from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up the database connection
engine = create_engine('sqlite:///arbitrage_bot.db')
Session = sessionmaker(bind=engine)
session = Session()