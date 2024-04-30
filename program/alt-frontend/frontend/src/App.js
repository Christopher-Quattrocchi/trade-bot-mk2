import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
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

const App = () => {
  return (
    <Router>
      <div>
        <Header />
        <Switch>
          <Route exact path="/" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/profile" component={ProfileInfo} />
          <Route path="/update-profile" component={UpdateProfile} />
          <Route path="/connect-dex" component={ConnectDEX} />
          <Route path="/dex-accounts" component={DEXAccounts} />
          <Route path="/dex-balances" component={DEXBalances} />
          <Route path="/arbitrage-opportunities" component={ArbitrageOpportunities} />
        </Switch>
        <Footer />
      </div>
    </Router>
  );
};

export default App;