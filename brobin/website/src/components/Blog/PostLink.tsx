import React from "react";
import dayjs from "dayjs";
import Link from "../Link";
import { BlogPost } from "../../types/Blog";

interface PostLinkProps {
  post: BlogPost;
}

const PostLink: React.FC<PostLinkProps> = (props) => {
  const post = props.post;
  const date = dayjs(post.created);

  return (
    <Link to={`/blog/${date.format("YYYY/MM")}/${post.slug}`}>
      {post.title}
    </Link>
  );
};

export default PostLink;
