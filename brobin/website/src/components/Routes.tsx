import React from 'react';
import { Route, Switch } from 'react-router-dom'
import Index from './Index';

const Routes: React.FC = () => {
  return (
    <Switch>
      <Route path="/" component={Index}/>
    </Switch>
  );
}

export default Routes;
