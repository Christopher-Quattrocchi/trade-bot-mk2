import React, { useEffect, useState } from 'react';
import { Box, Typography, List, ListItem, ListItemText } from '@mui/material';
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
        DEX Accounts
      </Typography>
      <List>
        {accounts.map((account) => (
          <ListItem key={account.id}>
            <ListItemText primary={`Exchange: ${account.exchange_name}`} />
          </ListItem>
        ))}
      </List>
    </Box>
  );
};

export default DEXAccounts;