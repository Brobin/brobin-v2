import {
  Badge,
  Card,
  CardContent,
  createStyles,
  makeStyles,
  Theme,
  Typography,
  withStyles,
} from "@material-ui/core";
import React, { useState } from "react";
import {
  BlogArchive,
  BlogCategory,
  BlogPost,
  BlogSidebarResponse,
} from "../../types/Blog";
import api from "../../utils/api";
import PostLink from "./PostLink";
import Link from "../Link";
import { useLoader } from "../../utils/hooks";

const YearBadge = withStyles((theme: Theme) =>
  createStyles({
    badge: {
      right: -15,
      top: 10,
      border: `2px solid ${theme.palette.background.paper}`,
      padding: "0 4px",
    },
  })
)(Badge);

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    card: {
      margin: theme.spacing(3),
      marginLeft: 0,
    },
  })
);

const BlogSidebar: React.FC = () => {
  const classes = useStyles();

  const [recentPosts, setRecentPosts] = useState<Array<BlogPost>>([]);
  const [categories, setCategories] = useState<Array<BlogCategory>>([]);
  const [archiveYears, setArchiveYears] = useState<Array<BlogArchive>>([]);

  const loadSidebar = async () => {
    const data: BlogSidebarResponse = await api.getBlogSidebar();
    setRecentPosts(data.recent);
    setCategories(data.categories);
    setArchiveYears(data.archive);
  };

  const { loaded } = useLoader(loadSidebar);

  return (
    <Card className={classes.card}>
      <CardContent>
        <Typography variant="h6">Recent Posts</Typography>
        {loaded &&
          recentPosts.map((post) => {
            return (
              <p key={post.id}>
                <PostLink post={post} />
              </p>
            );
          })}
        <Typography variant="h6">Categories</Typography>
        <p>
          {loaded &&
            categories.map((category, index) => {
              return (
                <span key={category.slug}>
                  {index > 0 ? ", " : ""}
                  <Link to={`/blog/${category.slug}`}>{category.title}</Link>
                </span>
              );
            })}
        </p>
        <Typography variant="h6">Archive</Typography>
        {loaded &&
          archiveYears.map((year) => {
            return (
              <div key={year.year}>
                <Link to={`/blog/archive/${year.year}`}>
                  <YearBadge badgeContent={year.posts} color="secondary">
                    {year.year}
                  </YearBadge>
                </Link>
                <br />
              </div>
            );
          })}
      </CardContent>
    </Card>
  );
};

export default BlogSidebar;
