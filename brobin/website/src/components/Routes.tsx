import React from "react";
import { Route, Switch } from "react-router-dom";
import PostPage from "./Blog/PostPage";
import BlogPage, {
  BlogArchivePage,
  BlogCategoryPage,
  BlogSearchPage,
} from "./Blog/BlogPage";

const Routes: React.FC = () => {
  return (
    <Switch>
      <Route
        exact
        path="/blog/:year/:month/:slug"
        render={(props) => {
          return <PostPage {...props} key={props.match.params.slug} />;
        }}
      />
      <Route exact path="/blog/archive/:year" component={BlogArchivePage} />
      <Route exact path="/blog/search" component={BlogSearchPage} />
      <Route exact path="/blog/:category" component={BlogCategoryPage} />
      <Route exact path="/blog" component={BlogPage} />
      <Route path="/" component={BlogPage} />
    </Switch>
  );
};

export default Routes;
