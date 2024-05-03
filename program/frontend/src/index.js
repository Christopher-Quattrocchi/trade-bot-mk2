import React from 'react';
import ReactDOM from 'react-dom';
import Register from './components/Auth/Register';
import ProfileInfo from './components/Profile/ProfileInfo';
import UpdateProfile from './components/Profile/UpdateProfile';
import ConnectDEX from './components/DEX/ConnectDEX';
import DEXAccounts from './components/DEX/DEXAccounts';
import DEXBalances from './components/DEX/DEXBalances';
import ArbitrageOpportunities from './components/Arbitrage/ArbitrageOpportunities';

ReactDOM.render(
  <React.StrictMode>
    <Register />
    <ProfileInfo />
    <UpdateProfile />
    <ConnectDEX />
    <DEXAccounts />
    <DEXBalances />
    <ArbitrageOpportunities />
  </React.StrictMode>,
  document.getElementById('root')
);


// import React from 'react';
// import ReactDOM from 'react-dom/client';
// import './index.css';
// import App from './App';
// import reportWebVitals from './reportWebVitals';

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );

// // If you want to start measuring performance in your app, pass a function
// // to log results (for example: reportWebVitals(console.log))
// // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
