import React, { useCallback, useState } from "react";
import { LinearProgress } from "@material-ui/core";
import Pagination from "@material-ui/lab/Pagination";
import BlogContainer from "./BlogContainer";
import PostPreview from "./PostPreview";
import { BlogPostListResponse, BlogPost } from "../../types/Blog";
import { useLoader } from "../../utils/hooks";
import api from "../../utils/api";

const BlogPage: React.FC = () => {
  const [posts, setPosts] = useState<Array<BlogPost>>([]);
  const [count, setCount] = useState<number>();
  const [page, setPage] = useState<number>(1);

  const loadBlogPosts = useCallback(async () => {
    const data: BlogPostListResponse = await api.listPosts({ page });
    setPosts(data.results);
    setCount(Math.ceil(data.count / 10));
  }, [page]);

  const { loaded, setLoaded } = useLoader(loadBlogPosts);

  return !loaded ? (
    <LinearProgress color="secondary" />
  ) : (
    <>
      <BlogContainer>
        {posts.map((post, index) => {
          return <PostPreview key={post.id} post={post} />;
        })}
      </BlogContainer>

      <Pagination
        count={count}
        page={page}
        onChange={(event, page: number) => {
          setPage(page);
          setLoaded(false);
        }}
      />
    </>
  );
};

export default BlogPage;
