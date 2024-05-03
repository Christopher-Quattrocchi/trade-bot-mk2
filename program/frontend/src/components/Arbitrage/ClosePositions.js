import React, { useEffect, useState } from 'react';
import {
  Box,
  Typography,
  Button,
  List,
  ListItem,
  ListItemText,
} from '@mui/material';
import { getOpenPositions, closeArbitragePosition } from '../../services/api';

const ClosePositions = () => {
  const [openPositions, setOpenPositions] = useState([]);

  useEffect(() => {
    const fetchOpenPositions = async () => {
      try {
        const data = await getOpenPositions();
        setOpenPositions(data.positions);
      } catch (error) {
        // Handle error
      }
    };

    fetchOpenPositions();
  }, []);

  const handleClosePosition = async (position) => {
    try {
      await closeArbitragePosition(position);
      // Handle successful position closing
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
        Close Arbitrage Positions
      </Typography>
      <List>
        {openPositions.map((position) => (
          <ListItem key={position.id}>
            <ListItemText
              primary={`Symbol: ${position.symbol}`}
              secondary={
                <>
                  <Typography component="span">
                    Buy Exchange: {position.buy_exchange}
                  </Typography>
                  <br />
                  <Typography component="span">
                    Sell Exchange: {position.sell_exchange}
                  </Typography>
                </>
              }
            />
            <Button
              variant="contained"
              color="primary"
              onClick={() => handleClosePosition(position)}
            >
              Close Position
            </Button>
          </ListItem>
        ))}
      </List>
    </Box>
  );
};

export default ClosePositions;