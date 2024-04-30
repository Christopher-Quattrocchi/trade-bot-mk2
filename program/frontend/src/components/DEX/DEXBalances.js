import React, { useEffect, useState } from 'react';
import { getDEXBalances } from '../../services/api';

const DEXBalances = () => {
  const [balances, setBalances] = useState([]);

  useEffect(() => {
    const fetchDEXBalances = async () => {
      try {
        const data = await getDEXBalances();
        setBalances(data.balances);
      } catch (error) {
        // Handle error
      }
    };

    fetchDEXBalances();
  }, []);

  return (
    <div>
      <h2>DEX Balances</h2>
      {balances.map((balance) => (
        <div key={balance.exchange_name}>
          <p>Exchange: {balance.exchange_name}</p>
          {/* Display token balances */}
        </div>
      ))}
    </div>
  );
};

export default DEXBalances;