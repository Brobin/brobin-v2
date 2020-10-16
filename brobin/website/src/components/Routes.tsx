import React from 'react';
import { Route, Switch } from 'react-router-dom'
import BlogPage from './Blog/BlogPage';

const Routes: React.FC = () => {
  return (
    <Switch>
      <Route path="/" component={BlogPage}/>
    </Switch>
  );
}

export default Routes;
