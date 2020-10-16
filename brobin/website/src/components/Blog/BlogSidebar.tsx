import React from 'react';
import { Card, CardContent, createStyles, makeStyles, Theme, Typography } from '@material-ui/core';


const useStyles = makeStyles((theme: Theme) => createStyles({
  card: {
    margin: theme.spacing(3)
  },
}));


const BlogSidebar: React.FC = () => {
  const classes = useStyles();

  return (
    <Card className={classes.card}>
      <CardContent>
        <Typography variant="h6">Recent Posts</Typography>
        <Typography variant="h6">Categories</Typography>
        <Typography variant="h6">Archive</Typography>
      </CardContent>
    </Card>
  )
};

export default BlogSidebar;
