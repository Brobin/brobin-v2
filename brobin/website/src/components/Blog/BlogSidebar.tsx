import {
  Badge,
  Card,
  CardContent,
  createStyles,
  Link,
  makeStyles,
  Theme,
  Typography,
} from "@material-ui/core";
import React, { useEffect, useState } from "react";
import {
  BlogArchive,
  BlogCategory,
  BlogPost,
  BlogSidebarResponse,
} from "../../types/Blog";
import api from "../../utils/api";
import PostLink from "./PostLink";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    card: {
      margin: theme.spacing(3),
    },
  })
);

const BlogSidebar: React.FC = () => {
  const classes = useStyles();

  const [loaded, setLoaded] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);

  const [recentPosts, setRecentPosts] = useState<Array<BlogPost>>([]);
  const [categories, setCategories] = useState<Array<BlogCategory>>([]);
  const [archiveYears, setArchiveYears] = useState<Array<BlogArchive>>([]);

  const loadSidebar = async () => {
    setLoading(true);
    const data: BlogSidebarResponse = await api.getBlogSidebar();

    setRecentPosts(data.recent);
    setCategories(data.categories);
    setArchiveYears(data.archive);

    setLoaded(true);
    setLoading(false);
  };

  useEffect(() => {
    if (!loaded && !loading) {
      loadSidebar();
    }
  }, [loaded, loading]);

  return (
    <Card className={classes.card}>
      <CardContent>
        <Typography variant="h6">Recent Posts</Typography>
        {loaded &&
          recentPosts.map((post) => {
            return <PostLink post={post} key={post.id} />;
          })}
        <Typography variant="h6">Categories</Typography>
        <p>
          {loaded &&
            categories.map((category, index) => {
              return (
                <span key={category.slug}>
                  {index > 0 ? ", " : ""}
                  <Link href={`/blog/${category.slug}`} color="secondary">
                    {category.title}
                  </Link>
                </span>
              );
            })}
        </p>
        <Typography variant="h6">Archive</Typography>
        {loaded &&
          archiveYears.map((year) => {
            return (
              <p key={year.year}>
                {year.year}&nbsp;
                <Badge badgeContent={year.posts} color="secondary" />
              </p>
            );
          })}
      </CardContent>
    </Card>
  );
};

export default BlogSidebar;
