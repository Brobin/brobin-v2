import React, { useCallback, useState } from "react";
import { RouteComponentProps } from "react-router-dom";
import { LinearProgress } from "@material-ui/core";
import Pagination from "@material-ui/lab/Pagination";
import BlogContainer from "./BlogContainer";
import PostPreview from "./PostPreview";
import { BlogPostListResponse, BlogPost } from "../../types/Blog";
import { useLoader } from "../../utils/hooks";
import api from "../../utils/api";

type BlogPageProps = {
  year?: string;
  category?: string;
};

const BaseBlogPage: React.FC<BlogPageProps> = (props) => {
  const year = props.year;
  const category = props.category;

  const [posts, setPosts] = useState<Array<BlogPost>>([]);
  const [count, setCount] = useState<number>();
  const [page, setPage] = useState<number>(1);

  const loadBlogPosts = useCallback(async () => {
    const data: BlogPostListResponse = await api.listPosts({
      page,
      year,
      category,
    });
    setPosts(data.results);
    setCount(Math.ceil(data.count / 10));
  }, [page, year, category]);

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

interface ArchiveProps {
  year: string;
}

const BlogArchivePage: React.FC<RouteComponentProps<ArchiveProps>> = ({
  match,
}) => {
  const year = match.params.year;
  return <BaseBlogPage year={year} key={year} />;
};

interface CategoryProps {
  category: string;
}

const BlogCategoryPage: React.FC<RouteComponentProps<CategoryProps>> = ({
  match,
}) => {
  const category = match.params.category;
  return <BaseBlogPage category={category} key={category} />;
};

const BlogPage: React.FC = () => <BaseBlogPage key={"base"} />;

export default BlogPage;
export { BlogArchivePage, BlogCategoryPage };
