import React, { useState } from "react";
import dayjs from "dayjs";
import { RouteComponentProps } from "react-router-dom";
import BlogContainer from "./BlogContainer";
import { BlogPost, BlogPostDetailParams } from "../../types/Blog";
import api from "../../utils/api";
import { useLoader } from "../../utils/hooks";
import {
  Card,
  CardContent,
  createStyles,
  makeStyles,
  Theme,
  Typography,
} from "@material-ui/core";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    card: {
      margin: theme.spacing(3),
      marginRight: 0,
    },
    hr: {
      border: "none",
      borderBottom: "1px solid #888",
    },
  })
);

const PostPage: React.FC<RouteComponentProps<BlogPostDetailParams>> = ({
  match,
}) => {
  const classes = useStyles();
  const [post, setPost] = useState<BlogPost>();

  const loadPost = async () => {
    const _post: BlogPost = await api.getPost(match.params);
    setPost(_post);

    // Yes, this is all quite janky, but we have to do this in
    // order to run the code prettifier on the blog posts.
    var postContent = document.getElementById("post-content");
    if (postContent && _post) {
      postContent.innerHTML = _post.content;

      var addScript = document.createElement("script");
      addScript.setAttribute(
        "src",
        "//cdnjs.cloudflare.com/ajax/libs/prettify/r298/run_prettify.min.js"
      );
      document.body.appendChild(addScript);
    }
  };

  const { loaded } = useLoader(loadPost);

  return (
    <BlogContainer>
      <Card className={classes.card}>
        <CardContent>
          {loaded && post && (
            <>
              <Typography variant="h5">{post.title}</Typography>
              <p>{dayjs(post.created).format("MMMM D, YYYY")}</p>
              <hr className={classes.hr} />
            </>
          )}
          <span id="post-content" />
        </CardContent>
      </Card>
    </BlogContainer>
  );
};

export default PostPage;
