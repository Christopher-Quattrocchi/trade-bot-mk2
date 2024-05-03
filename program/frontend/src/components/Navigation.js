// import React from 'react';
// import { Link } from 'react-router-dom';

// const Navigation = () => {
//   return (
//     <nav style={{ padding: '20px 0', background: '#f0f0f0', marginBottom: '20px' }}>
//       <Link to="/" style={{ marginRight: '10px' }}>Home</Link>
//       <Link to="/login" style={{ marginRight: '10px' }}>Login</Link>
//       <Link to="/register" style={{ marginRight: '10px' }}>Register</Link>
//       <Link to="/profile" style={{ marginRight: '10px' }}>Profile</Link>
//       <Link to="/update-profile" style={{ marginRight: '10px' }}>Update Profile</Link>
//       <Link to="/connect-dex" style={{ marginRight: '10px' }}>Connect DEX</Link>
//       <Link to="/dex-accounts" style={{ marginRight: '10px' }}>DEX Accounts</Link>
//       <Link to="/dex-balances" style={{ marginRight: '10px' }}>DEX Balances</Link>
//       <Link to="/arbitrage-opportunities" style={{ marginRight: '10px' }}>Arbitrage Opportunities</Link>
//     </nav>
//   );
// };

// export default Navigation;

// import React from 'react';
// import { Link as RouterLink } from 'react-router-dom';
// import { Box, Link, Typography } from '@mui/material';

// const Navigation = () => {
//   return (
//     <Box sx={{ padding: '20px 0', backgroundColor: 'background.default', marginBottom: '20px', display: 'flex', justifyContent: 'center' }}>
//       <Link component={RouterLink} to="/" sx={{ marginRight: '10px', color: 'text.primary' }}>Home</Link>
//       <Link component={RouterLink} to="/login" sx={{ marginRight: '10px', color: 'text.primary' }}>Login</Link>
//       <Link component={RouterLink} to="/register" sx={{ marginRight: '10px', color: 'text.primary' }}>Register</Link>
//       <Link component={RouterLink} to="/profile" sx={{ marginRight: '10px', color: 'text.primary' }}>Profile</Link>
//       <Link component={RouterLink} to="/update-profile" sx={{ marginRight: '10px', color: 'text.primary' }}>Update Profile</Link>
//       <Link component={RouterLink} to="/connect-dex" sx={{ marginRight: '10px', color: 'text.primary' }}>Connect DEX</Link>
//       <Link component={RouterLink} to="/dex-accounts" sx={{ marginRight: '10px', color: 'text.primary' }}>DEX Accounts</Link>
//       <Link component={RouterLink} to="/dex-balances" sx={{ marginRight: '10px', color: 'text.primary' }}>DEX Balances</Link>
//       <Link component={RouterLink} to="/arbitrage-opportunities" sx={{ marginRight: '10px', color: 'text.primary' }}>Arbitrage Opportunities</Link>
//     </Box>
//   );
// };

// export default Navigation;


import React from 'react';
import { Link as RouterLink } from 'react-router-dom'; // Import Link as RouterLink to avoid naming conflicts
import { Box, Link, Typography } from '@mui/material';

const Navigation = () => {
  return (
    <Box sx={{
      padding: '20px 0',
      backgroundColor: 'background.paper', // Directly use the theme color here
      marginBottom: '20px',
      display: 'flex',
      justifyContent: 'center'
    }}>
      <Link component={RouterLink} to="/" sx={{ mx: 2, typography: 'h6', color: 'text.primary' }}>Home</Link>
      <Link component={RouterLink} to="/login" sx={{ mx: 2, typography: 'h6', color: 'text.primary' }}>Login</Link>
      <Link component={RouterLink} to="/register" sx={{ mx: 2, typography: 'h6', color: 'text.primary' }}>Register</Link>
      <Link component={RouterLink} to="/profile" sx={{ mx: 2, typography: 'h6', color: 'text.primary' }}>Profile</Link>
      <Link component={RouterLink} to="/update-profile" sx={{ mx: 2, typography: 'h6', color: 'text.primary' }}>Update Profile</Link>
      <Link component={RouterLink} to="/connect-dex" sx={{ mx: 2, typography: 'h6', color: 'text.primary' }}>Connect DEX</Link>
      <Link component={RouterLink} to="/dex-accounts" sx={{ mx: 2, typography: 'h6', color: 'text.primary' }}>DEX Accounts</Link>
      <Link component={RouterLink} to="/dex-balances" sx={{ mx: 2, typography: 'h6', color: 'text.primary' }}>DEX Balances</Link>
      <Link component={RouterLink} to="/arbitrage-opportunities" sx={{ mx: 2, typography: 'h6', color: 'text.primary' }}>Arbitrage Opportunities</Link>
    </Box>
  );
};

export default Navigation;
