import React, { useEffect, useState } from 'react';
import request from 'request-promise-native';
import PostPreview from './PostPreview';
import { BlogListResponse, BlogPost } from '../../types/Blog';

const BlogPage: React.FC = () => {
  const [loaded, setLoaded] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);
  const [posts, setPosts] = useState<Array<BlogPost>>([]);

  const loadPage = async () => {
    setLoading(true);
    const requestOptions = {
      url: `http://127.0.0.1:8000/api/blog/posts/`,
      mehtod: 'GET',
      headers: {'Content-Type': 'application/json'}
    }
    const response = await request(requestOptions);
    const data: BlogListResponse = JSON.parse(response);

    setPosts(data.results)
    setLoaded(true);
    setLoading(false);
  }

  useEffect(() => {
    if(!loaded && !loading) {
      loadPage();
    }
  });

  return !loaded ? <>Loading</> : (
    <>
      {posts.map((post, index) => {
        return <PostPreview key={post.id} post={post}/>
      })}
    </>
  );
}

export default BlogPage;
