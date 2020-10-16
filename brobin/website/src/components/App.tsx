import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import { CssBaseline } from '@material-ui/core';
import Routes from './Routes';
import NavBar from './NavBar';
import Theme from './Theme';

const App: React.FC = () => (
  <BrowserRouter>
    <Theme>
      <CssBaseline/>
      <NavBar/>
      <Routes/>
    </Theme>
  </BrowserRouter>
);

export default App;
