import { Dayjs } from "dayjs";

export type BlogPost = {
  id: number;
  slug: string;
  created: Dayjs;
  updated: Dayjs;
  title: string;
  preview: string;
  content: string;
  category_id: number;
  author: number;
};

export type BlogPostListParams = {
  page: number;
};

export type BlogPostList = {
  count: number;
  next: string;
  previous: string;
  results: Array<BlogPost>;
};
