import React, { useEffect, useState } from 'react';
import { getArbitrageOpportunities } from '../../services/api';

const ArbitrageOpportunities = () => {
  const [opportunities, setOpportunities] = useState([]);

  useEffect(() => {
    const fetchArbitrageOpportunities = async () => {
      try {
        const data = await getArbitrageOpportunities();
        setOpportunities(data.opportunities);
      } catch (error) {
        // Handle error
      }
    };

    fetchArbitrageOpportunities();
  }, []);

  return (
    <div>
      <h2>Arbitrage Opportunities</h2>
      {opportunities.map((opportunity) => (
        <div key={opportunity.id}>
          <p>Symbol: {opportunity.symbol}</p>
          <p>Buy Exchange: {opportunity.buy_exchange}</p>
          <p>Sell Exchange: {opportunity.sell_exchange}</p>
          <p>Profit Percentage: {opportunity.profit_percentage}%</p>
        </div>
      ))}
    </div>
  );
};

export default ArbitrageOpportunities;