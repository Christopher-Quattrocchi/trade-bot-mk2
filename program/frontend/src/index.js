// import React from 'react';
// import ReactDOM from 'react-dom';
// import Register from './components/Auth/Register';
// import ProfileInfo from './components/Profile/ProfileInfo';
// import UpdateProfile from './components/Profile/UpdateProfile';
// import ConnectDEX from './components/DEX/ConnectDEX';
// import DEXAccounts from './components/DEX/DEXAccounts';
// import DEXBalances from './components/DEX/DEXBalances';
// import ArbitrageOpportunities from './components/Arbitrage/ArbitrageOpportunities';

// ReactDOM.render(
//   <React.StrictMode>
//     <Register />
//     <ProfileInfo />
//     <UpdateProfile />
//     <ConnectDEX />
//     <DEXAccounts />
//     <DEXBalances />
//     <ArbitrageOpportunities />
//   </React.StrictMode>,
//   document.getElementById('root')
// );

import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App'; // Ensure this path is correct

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      <App />
  </React.StrictMode>
);
