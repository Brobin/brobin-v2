import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import { Container, CssBaseline } from '@material-ui/core';
import Routes from './Routes';
import NavBar from './NavBar';
import Theme from './Theme';

const App: React.FC = () => (
  <BrowserRouter>
    <Theme>
      <CssBaseline/>
      <NavBar/>
      <Container>
        <Routes/>
      </Container>
    </Theme>
  </BrowserRouter>
);

export default App;
