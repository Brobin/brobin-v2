import React from "react";
import { Route, Switch } from "react-router-dom";
import PostPage from "./Blog/PostPage";
import BlogPage, {
  BlogArchivePage,
  BlogCategoryPage,
  BlogSearchPage,
} from "./Blog/BlogPage";
import CookbookPage from "./Cookbook/CookbookPage";
import RecipePage from "./Cookbook/RecipePage";
import StatsPage from "./Fishing/StatsPage";
import ErrorBoundary from "./Error/ErrorBoundary";
import { Error404 } from "./Error/Error";

const Routes: React.FC = () => {
  return (
    <ErrorBoundary>
      <Switch>
        <Route
          exact
          path="/blog/:year/:month/:slug"
          render={(props): React.ReactNode => {
            return <PostPage {...props} key={props.match.params.slug} />;
          }}
        />
        <Route exact path="/blog/archive/:year" component={BlogArchivePage} />
        <Route exact path="/blog/search" component={BlogSearchPage} />
        <Route exact path="/blog/:category" component={BlogCategoryPage} />
        <Route exact path="/blog" component={BlogPage} />
        <Route exact path="/cookbook" component={CookbookPage} />
        <Route exact path="/recipe/:slug" component={RecipePage} />
        <Route exact path="/fishing" component={StatsPage} />
        <Route exact path="/" component={BlogPage} />
        <Route component={Error404} />
      </Switch>
    </ErrorBoundary>
  );
};

export default Routes;
