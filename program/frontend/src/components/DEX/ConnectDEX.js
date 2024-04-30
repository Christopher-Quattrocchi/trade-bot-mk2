import React, { useState } from 'react';
import { connectDEXAccount } from '../../services/api';

const ConnectDEX = () => {
  const [exchangeName, setExchangeName] = useState('');
  const [apiKey, setApiKey] = useState('');
  const [apiSecret, setApiSecret] = useState('');

  const handleConnectDEX = async (e) => {
    e.preventDefault();
    try {
      await connectDEXAccount(exchangeName, apiKey, apiSecret);
      // Handle successful DEX account connection
    } catch (error) {
      // Handle error
    }
  };

  return (
    <div>
      <h2>Connect DEX Account</h2>
      <form onSubmit={handleConnectDEX}>
        <input
          type="text"
          placeholder="Exchange Name"
          value={exchangeName}
          onChange={(e) => setExchangeName(e.target.value)}
        />
        <input
          type="text"
          placeholder="API Key"
          value={apiKey}
          onChange={(e) => setApiKey(e.target.value)}
        />
        <input
          type="text"
          placeholder="API Secret"
          value={apiSecret}
          onChange={(e) => setApiSecret(e.target.value)}
        />
        <button type="submit">Connect DEX Account</button>
      </form>
    </div>
  );
};

export default ConnectDEX;