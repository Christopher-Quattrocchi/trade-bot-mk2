import { Toolbar, Typography, Link } from '@mui/material';


return (

  <Toolbar position="fixed" variant="dense" style={styles.navbar}>

    <Link href="/" style={styles.link}>

      <Typography variant="h6" color="inherit">

        {'Crypto-Arb-Bot-mk2'}

      </Typography>

    </Link>

    <div style={styles.links}>

      {/* {add links}  */}

    </div>

  </Toolbar>

);