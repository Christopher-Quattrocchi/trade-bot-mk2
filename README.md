# trade-bot-mk2 (WIP)

## Table of Contents

- [About](#about)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Known Bugs](#known-bugs)
- [Feedback](#feedback)
- [License](#license)

## About (NOTE: This is very much a WIP. I do not recommend running it at this time.)

This project is a full-stack web application designed as an Arbitrage Bot capable of identifying and executing arbitrage opportunities across multiple cryptocurrency exchanges and blockchain networks. Unlike Mk1 (a fully autonomous 24/7 bot with self directed behavior), this bot is user directed and does not operate autonomously. It combines a frontend built with React and a backend implemented using Flask, Axios, Python, CCXT, Stargate and various libraries for interacting with exchanges and blockchains.

## Features (some features are incomplete!)

- **Exchange Connections:** Connect to multiple cryptocurrency exchanges using their APIs and the CCXT library.
- **Market Data Fetching:** Retrieve real-time market data, including order books and trade history, from connected exchanges.
- **Arbitrage Analysis:** Analyze market data and identify potential arbitrage opportunities based on specified profit percentage thresholds.
- **Position Management:** Open and close arbitrage positions by placing buy and sell orders on different exchanges.
- **Cross-Chain Token Transfers:** Leverage the Stargate protocol to bridge tokens across different blockchain networks during the execution of arbitrage positions.
- **User Authentication:** Register, login, and manage user profiles through the frontend interface.
- **DEX Account Management:** Connect decentralized exchange (DEX) accounts, view connected accounts, and fetch account balances.
- **User Interface:** The frontend provides a user-friendly interface for viewing arbitrage opportunities, opening and closing positions, and managing DEX accounts.

## Technologies Used

### Frontend

- **React:** JavaScript library for building user interfaces.
- **React Router DOM:** Library for routing in React applications.
- **Material UI:** UI component library for React.
- **Axios:** Promise-based HTTP client for making API calls.

### Backend

- **Flask:** Python web framework for building the backend API.
- **SQLAlchemy:** Object-relational mapping (ORM) for interacting with the database.
- **Flask-JWT-Extended:** JWT authentication library for Flask.
- **CCXT:** Cryptocurrency Exchange Trading Library for interacting with exchange APIs.
- **Web3:** Python library for interacting with Ethereum-based blockchains and smart contracts.
- **Stargate:** Cross-chain bridge protocol for transferring tokens across different blockchain networks.

## Installation (WIP!! I would *strongly* recommend waiting until future updates before attempting to run this)

Follow these steps to set up the project locally:

1. **Clone the repository to your local machine:**
   git clone https://github.com/Christopher-Quattrocchi/trade-bot-mk2.git

2. **Navigate to project directory:**
   cd trade-bot-mk2, cd program

3. **Install Python packages**
   cd backend
   pip install -r requirements.txt

4. **Set up environmental variables for exchange API keys, Stargate config, and Telegram**

5. **Run the Flask Application**
   python app.py in terminal

## Front end setup

1. **Navigate to front end**
   cd .., cd frontend

2. **Install required Node.js packages**
   npm install
  
3. **Start the React dev server**
   npm run start

4. **Open web browser and navigate to http://localhost:3000**

## Known Bugs 
This is a WIP, I would suggest waiting until this is complete to try to run it.

## Feedback
chrisquattrocchi@gmail.com suggestions welcome!

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Copyright (C) 2024 Chris Quattrocchi

```
MIT License

Copyright (c) 2023 Chris Quattrochi, Simi Oyin, Jonathan Song, Trent Dietzel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.