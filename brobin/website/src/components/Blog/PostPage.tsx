import React, { useState } from "react";
import dayjs from "dayjs";
import { RouteComponentProps } from "react-router-dom";
import BlogContainer from "./BlogContainer";
import { BlogPost, BlogPostDetailParams } from "../../types/Blog";
import api from "../../utils/api";
import { useLoader } from "../../utils/hooks";
import { Typography } from "@material-ui/core";

const PostPage: React.FC<RouteComponentProps<BlogPostDetailParams>> = ({
  match,
}) => {
  const [post, setPost] = useState<BlogPost>();

  const loadPost = async () => {
    const _post: BlogPost = await api.getPost(match.params);
    setPost(_post);
  };

  const { loaded } = useLoader(loadPost);

  return (
    <BlogContainer>
      {loaded && post && (
        <>
          <br />
          <Typography variant="h5">{post.title}</Typography>
          <p>{dayjs(post.created).format("MMMM D, YYYY")}</p>
          <hr />
          <span dangerouslySetInnerHTML={{ __html: post.content }} />
        </>
      )}
    </BlogContainer>
  );
};

export default PostPage;
