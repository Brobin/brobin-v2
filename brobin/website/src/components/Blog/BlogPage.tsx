import React, { useCallback, useEffect, useState } from "react";
import { LinearProgress } from "@material-ui/core";
import Pagination from "@material-ui/lab/Pagination";
import BlogContainer from "./BlogContainer";
import PostPreview from "./PostPreview";
import { BlogPostList, BlogPost } from "../../types/Blog";
import api from "../../utils/api";

const BlogPage: React.FC = () => {
  const [loaded, setLoaded] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);

  const [posts, setPosts] = useState<Array<BlogPost>>([]);
  const [count, setCount] = useState<number>();
  const [page, setPage] = useState<number>(1);

  const loadPage = useCallback(async () => {
    setLoading(true);
    const data: BlogPostList = await api.listPosts({ page });

    setPosts(data.results);
    setCount(Math.ceil(data.count / 10));
    setLoaded(true);
    setLoading(false);
  }, [page]);

  useEffect(() => {
    if (!loaded && !loading) {
      loadPage();
    }
  }, [loaded, loading, loadPage]);

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
