import { Dayjs } from "dayjs";
import { StringLiteral } from "typescript";

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

export type BlogCategory = {
  title: string;
  slug: string;
};

export type BlogArchive = {
  year: number;
  posts: number;
};

export type BlogPostListParams = {
  page: number;
  year?: string;
  category?: string;
};

export type BlogPostListResponse = {
  count: number;
  next: string;
  previous: string;
  results: Array<BlogPost>;
};

export type BlogPostDetailParams = {
  year: string;
  month: string;
  slug: string;
};

export type BlogSidebarResponse = {
  recent: Array<BlogPost>;
  categories: Array<BlogCategory>;
  archive: Array<BlogArchive>;
};
