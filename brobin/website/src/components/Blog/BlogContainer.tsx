import React from "react";
import {
  Card,
  CardContent,
  Container,
  createStyles,
  Grid,
  makeStyles,
  Theme,
  Typography,
} from "@material-ui/core";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    card: {
      margin: theme.spacing(3),
    },
  })
);

const BlogContainer: React.FC = ({ children }) => {
  const classes = useStyles();

  return (
    <Container>
      <Grid container spacing={3}>
        <Grid item sm={8}>
          {children}
        </Grid>
        <Grid item sm={4}>
          <Card className={classes.card}>
            <CardContent>
              <Typography variant="h6">Recent Posts</Typography>
              <Typography variant="h6">Categories</Typography>
              <Typography variant="h6">Archive</Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
};

export default BlogContainer;
