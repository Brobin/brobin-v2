import React from "react";
import { Route, Switch } from "react-router-dom";
import { BlogPage, PostPage } from "./Blog";

const Routes: React.FC = () => {
  return (
    <Switch>
      <Route path="/blog/:year/:month/:slug" component={PostPage} />
      <Route path="/blog" component={BlogPage} />
      <Route path="/" component={BlogPage} />
    </Switch>
  );
};

export default Routes;
