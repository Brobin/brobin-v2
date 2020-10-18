import React from "react";
import dayjs from "dayjs";
import { Link } from "@material-ui/core";
import { BlogPost } from "../../types/Blog";

interface PostLinkProps {
  post: BlogPost;
}

const PostLink: React.FC<PostLinkProps> = (props) => {
  const post = props.post;
  const date = dayjs(post.created);

  return (
    <Link
      href={`/blog/${date.format("YYYY/MM")}/${post.slug}`}
      color="secondary"
    >
      {post.title}
    </Link>
  );
};

export default PostLink;
