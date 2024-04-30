import React, { useEffect, useState } from 'react';
import { getDEXAccounts } from '../../services/api';

const DEXAccounts = () => {
  const [accounts, setAccounts] = useState([]);

  useEffect(() => {
    const fetchDEXAccounts = async () => {
      try {
        const data = await getDEXAccounts();
        setAccounts(data.accounts);
      } catch (error) {
        // Handle error
      }
    };

    fetchDEXAccounts();
  }, []);

  return (
    <div>
      <h2>DEX Accounts</h2>
      {accounts.map((account) => (
        <div key={account.id}>
          <p>Exchange: {account.exchange_name}</p>
        </div>
      ))}
    </div>
  );
};

export default DEXAccounts;