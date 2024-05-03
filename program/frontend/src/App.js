import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import ProfileInfo from './components/Profile/ProfileInfo';
import UpdateProfile from './components/Profile/UpdateProfile';
import ConnectDEX from './components/DEX/ConnectDEX';
import DEXAccounts from './components/DEX/DEXAccounts';
import DEXBalances from './components/DEX/DEXBalances';
import ArbitrageOpportunities from './components/Arbitrage/ArbitrageOpportunities';
import Header from './components/Layout/Header';
import Footer from './components/Layout/Footer';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import theme from './theme/theme';

const App = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <div>
          <Header />
          <Routes>
            <Route path="/" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/profile" element={<ProfileInfo />} />
            <Route path="/update-profile" element={<UpdateProfile />} />
            <Route path="/connect-dex" element={<ConnectDEX />} />
            <Route path="/dex-accounts" element={<DEXAccounts />} />
            <Route path="/dex-balances" element={<DEXBalances />} />
            <Route path="/arbitrage-opportunities" element={<ArbitrageOpportunities />} />
          </Routes>
          <Footer />
        </div>
      </Router>
    </ThemeProvider>
  );
};

export default App;