import React, { useEffect, useState } from 'react';
import {
  Box,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from '@mui/material';
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
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        maxWidth: 800,
        mx: 'auto',
        my: 4,
        p: 4,
        bgcolor: 'background.paper',
        borderRadius: 2,
        boxShadow: 2,
      }}
    >
      <Typography variant="h5" component="h1" gutterBottom>
        Arbitrage Opportunities
      </Typography>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Symbol</TableCell>
              <TableCell>Buy Exchange</TableCell>
              <TableCell>Buy Price</TableCell>
              <TableCell>Sell Exchange</TableCell>
              <TableCell>Sell Price</TableCell>
              <TableCell>Amount</TableCell>
              <TableCell>Profit Percentage</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {opportunities.map((opportunity) => (
              <TableRow key={opportunity.symbol}>
                <TableCell>{opportunity.symbol}</TableCell>
                <TableCell>{opportunity.buy_exchange}</TableCell>
                <TableCell>{opportunity.buy_price}</TableCell>
                <TableCell>{opportunity.sell_exchange}</TableCell>
                <TableCell>{opportunity.sell_price}</TableCell>
                <TableCell>{opportunity.amount}</TableCell>
                <TableCell>{opportunity.profit_percentage}%</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default ArbitrageOpportunities;