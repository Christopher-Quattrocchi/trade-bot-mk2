import React from 'react';
import { Box, Typography } from '@mui/material';

const Footer = () => {
  return (
    <Box sx={{ bgcolor: 'background.paper', p: 6 }} component="footer">
      <Typography variant="body2" color="text.secondary" align="center">
        {'Copyright © '}
        Arbitrage Bot Mk2 {new Date().getFullYear()}
        {'.'}
      </Typography>
    </Box>
  );
};

export default Footer;