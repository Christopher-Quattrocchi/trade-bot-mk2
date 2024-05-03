import React, { useState } from 'react';
import {
  Box,
  Typography,
  TextField,
  Button,
  List,
  ListItem,
  ListItemText,
} from '@mui/material';
import { openArbitragePosition } from '../../services/api';

const OpenPositions = ({ opportunities }) => {
  const [selectedOpportunity, setSelectedOpportunity] = useState(null);
  const [amount, setAmount] = useState('');

  const handleOpenPosition = async (opportunity) => {
    try {
      await openArbitragePosition(opportunity, amount);
      // Handle successful position opening
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
        Open Arbitrage Positions
      </Typography>
      <List>
        {opportunities.map((opportunity) => (
          <ListItem
            key={opportunity.id}
            button
            onClick={() => setSelectedOpportunity(opportunity)}
          >
            <ListItemText
              primary={`Symbol: ${opportunity.symbol}`}
              secondary={`Profit Percentage: ${opportunity.profit_percentage}%`}
            />
          </ListItem>
        ))}
      </List>
      {selectedOpportunity && (
        <Box sx={{ mt: 4, width: '100%' }}>
          <Typography variant="h6" gutterBottom>
            Selected Opportunity
          </Typography>
          <Typography variant="body1" gutterBottom>
            {`Symbol: ${selectedOpportunity.symbol}`}
          </Typography>
          <Typography variant="body1" gutterBottom>
            {`Buy Exchange: ${selectedOpportunity.buy_exchange}`}
          </Typography>
          <Typography variant="body1" gutterBottom>
            {`Buy Price: ${selectedOpportunity.buy_price}`}
          </Typography>
          <Typography variant="body1" gutterBottom>
            {`Sell Exchange: ${selectedOpportunity.sell_exchange}`}
          </Typography>
          <Typography variant="body1" gutterBottom>
            {`Sell Price: ${selectedOpportunity.sell_price}`}
          </Typography>
          <TextField
            label="Amount"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            margin="normal"
            fullWidth
          />
          <Button
            variant="contained"
            color="primary"
            onClick={() => handleOpenPosition(selectedOpportunity)}
            sx={{ mt: 2 }}
          >
            Open Position
          </Button>
        </Box>
      )}
    </Box>
  );
};

export default OpenPositions;