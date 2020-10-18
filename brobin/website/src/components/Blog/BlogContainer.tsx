import React from "react";
import { Container, Grid } from "@material-ui/core";
import BlogSidebar from "./BlogSidebar";

const BlogContainer: React.FC = ({ children }) => (
  <Container>
    <Grid container spacing={3}>
      <Grid item sm={8}>
        {children}
      </Grid>
      <Grid item sm={4}>
        <BlogSidebar />
      </Grid>
    </Grid>
  </Container>
);

export default BlogContainer;
