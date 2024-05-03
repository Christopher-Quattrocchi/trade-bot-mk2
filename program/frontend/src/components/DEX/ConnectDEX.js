import React, { useState } from 'react';
import { Box, Typography, TextField, Button } from '@mui/material';
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
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        maxWidth: 400,
        mx: 'auto',
        my: 4,
        p: 4,
        bgcolor: 'background.paper',
        borderRadius: 2,
        boxShadow: 2,
      }}
    >
      <Typography variant="h5" component="h1" gutterBottom>
        Connect DEX Account
      </Typography>
      <form onSubmit={handleConnectDEX}>
        <TextField
          label="Exchange Name"
          value={exchangeName}
          onChange={(e) => setExchangeName(e.target.value)}
          margin="normal"
          fullWidth
        />
        <TextField
          label="API Key"
          value={apiKey}
          onChange={(e) => setApiKey(e.target.value)}
          margin="normal"
          fullWidth
        />
        <TextField
          label="API Secret"
          type="password"
          value={apiSecret}
          onChange={(e) => setApiSecret(e.target.value)}
          margin="normal"
          fullWidth
        />
        <Button
          type="submit"
          variant="contained"
          color="primary"
          fullWidth
          sx={{ mt: 2 }}
        >
          Connect DEX Account
        </Button>
      </form>
    </Box>
  );
};

export default ConnectDEX;