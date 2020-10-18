import React, { useCallback, useEffect, useState } from "react";
import request from "request-promise-native";
import { LinearProgress } from "@material-ui/core";
import Pagination from "@material-ui/lab/Pagination";
import BlogContainer from "./BlogContainer";
import PostPreview from "./PostPreview";
import { BlogListResponse, BlogPost } from "../../types/Blog";

const BlogPage: React.FC = () => {
  const [loaded, setLoaded] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);

  const [posts, setPosts] = useState<Array<BlogPost>>([]);
  const [count, setCount] = useState<number>();
  const [page, setPage] = useState<number>(1);

  const loadPage = useCallback(async () => {
    setLoading(true);
    const requestOptions = {
      url: `http://127.0.0.1:8000/api/blog/posts/?page=${page}`,
      mehtod: "GET",
      headers: { "Content-Type": "application/json" },
    };
    const response = await request(requestOptions);
    const data: BlogListResponse = JSON.parse(response);

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
