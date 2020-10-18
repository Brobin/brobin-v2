import React, { useCallback, useState } from "react";
import { RouteComponentProps } from "react-router-dom";
import {
  createStyles,
  Grid,
  LinearProgress,
  makeStyles,
  Theme,
  Typography,
} from "@material-ui/core";
import Pagination from "@material-ui/lab/Pagination";
import BlogContainer from "./BlogContainer";
import PostPreview from "./PostPreview";
import { BlogPostListResponse, BlogPost } from "../../types/Blog";
import { useLoader } from "../../utils/hooks";
import api from "../../utils/api";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    heading: {
      margin: theme.spacing(3),
    },
  })
);

type BlogPageProps = {
  query?: string;
  year?: string;
  category?: string;
};

const BaseBlogPage: React.FC<BlogPageProps> = (props) => {
  const classes = useStyles();
  const query = props.query;
  const year = props.year;
  const category = props.category;

  const [posts, setPosts] = useState<Array<BlogPost>>([]);
  const [count, setCount] = useState<number>();
  const [page, setPage] = useState<number>(1);

  const loadBlogPosts = useCallback(async () => {
    const data: BlogPostListResponse = await api.listPosts({
      page,
      query,
      year,
      category,
    });
    setPosts(data.results);
    setCount(Math.ceil(data.count / 10));
  }, [page, year, category]);

  const { loaded, setLoaded } = useLoader(loadBlogPosts);

  return !loaded ? (
    <LinearProgress color="secondary" />
  ) : (
    <BlogContainer>
      {year && (
        <Typography variant="h5" className={classes.heading}>
          Posts from {year}
        </Typography>
      )}
      {category && (
        <Typography variant="h5" className={classes.heading}>
          Posts in "{category}"
        </Typography>
      )}
      {query && (
        <Typography variant="h5" className={classes.heading}>
          Search results for "{query}"
        </Typography>
      )}
      {posts.map((post, index) => {
        return <PostPreview key={post.id} post={post} />;
      })}

      <Grid
        container
        spacing={0}
        direction="column"
        alignItems="center"
        justify="center"
      >
        <Grid item xs={12}>
          <Pagination
            count={count}
            page={page}
            onChange={(event, page: number) => {
              setPage(page);
              setLoaded(false);
            }}
          />
        </Grid>
      </Grid>
    </BlogContainer>
  );
};

interface ArchiveProps {
  year: string;
}

const BlogArchivePage: React.FC<RouteComponentProps<ArchiveProps>> = ({
  match,
}) => {
  const year = match.params.year;
  return <BaseBlogPage year={year} key={year} />;
};

interface CategoryProps {
  category: string;
}

const BlogCategoryPage: React.FC<RouteComponentProps<CategoryProps>> = ({
  match,
}) => {
  const category = match.params.category;
  return <BaseBlogPage category={category} key={category} />;
};

interface SearchProps {
  category: string;
}

const BlogSearchPage: React.FC<RouteComponentProps<SearchProps>> = () => {
  const query = new URLSearchParams(window.location.search).get("q");
  return <BaseBlogPage query={query || undefined} key={query} />;
};

const BlogPage: React.FC = () => <BaseBlogPage key={"base"} />;

export default BlogPage;
export { BlogArchivePage, BlogCategoryPage, BlogSearchPage };
