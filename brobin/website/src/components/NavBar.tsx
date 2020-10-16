import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Container from '@material-ui/core/Container';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
  title: {
    flexGrow: 1,
  },
}));

const NavBar: React.FC = () => {
  const classes = useStyles();

  return (
    <AppBar position="static">
      <Container>
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            Brobin
          </Typography>
          <Button color="inherit">Blog</Button>
          <Button color="inherit">Projects</Button>
          <Button color="inherit">Cookbook</Button>
        </Toolbar>
      </Container>
    </AppBar>
  );
}

export default NavBar;
