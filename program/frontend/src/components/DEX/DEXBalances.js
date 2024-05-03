import React, { useEffect, useState } from 'react';
import {
  Box,
  Typography,
  List,
  ListItem,
  ListItemText,
  ListSubheader,
} from '@mui/material';
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
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        maxWidth: 600,
        mx: 'auto',
        my: 4,
        p: 4,
        bgcolor: 'background.paper',
        borderRadius: 2,
        boxShadow: 2,
      }}
    >
      <Typography variant="h5" component="h1" gutterBottom>
        DEX Balances
      </Typography>
      <List>
        {balances.map((balance) => (
          <ListItem key={balance.exchange_name}>
            <ListItemText
              primary={`Exchange: ${balance.exchange_name}`}
              primaryTypographyProps={{ variant: 'h6' }}
            />
            <List dense>
              {balance.balances.map((token) => (
                <ListItem key={token.symbol}>
                  <ListItemText
                    primary={`${token.symbol}: ${token.amount}`}
                    secondary={`Fiat Value: ${token.fiat_value}`}
                  />
                </ListItem>
              ))}
            </List>
          </ListItem>
        ))}
      </List>
    </Box>
  );
};

export default DEXBalances;