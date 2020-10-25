import request from "request-promise-native";
import {
  BlogPost,
  BlogPostDetailParams,
  BlogPostListParams,
  BlogPostListResponse,
  BlogSidebarResponse,
} from "../types/Blog";
import {
  Recipe,
  RecipeListResponse,
  RecipeDetailParams,
} from "../types/Cookbook";
import {
  FishingStatsResponse,
  FishingYearStatsResponse,
} from "../types/Fishing";

const baseUrl =
  process.env.NODE_ENV === "production"
    ? `${window.location.origin}/api`
    : "http://127.0.0.1:8000/api";

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const get = async (route: string): Promise<any> => {
  const requestOptions = {
    url: `${baseUrl}${route}`,
    method: "GET",
    headers: { "Content-Type": "application/json" },
  };
  const response = await request(requestOptions);
  return JSON.parse(response);
};

export const listPosts = async (
  params: BlogPostListParams
): Promise<BlogPostListResponse> => {
  if (params.category) {
    return get(`/blog/${params.category}/?page=${params.page}`);
  }
  if (params.year) {
    return get(`/blog/archive/${params.year}/`);
  }
  if (params.query) {
    return get(`/blog/search/?page${params.page}&query=${params.query}`);
  }
  return get(`/blog/?page=${params.page}`);
};

export const getPost = (params: BlogPostDetailParams): Promise<BlogPost> => {
  return get(`/blog/${params.year}/${params.month}/${params.slug}/`);
};

export const getBlogSidebar = (): Promise<BlogSidebarResponse> => {
  return get("/blog/sidebar/");
};

export const listRecipes = (): Promise<RecipeListResponse> => {
  return get(`/cookbook/`);
};

export const getRecipe = (params: RecipeDetailParams): Promise<Recipe> => {
  return get(`/cookbook/${params.slug}`);
};

export const getFishingStats = (): Promise<FishingStatsResponse> => {
  return get(`/fishing/`);
};

export const getFishingYearStats = (
  year: number
): Promise<FishingYearStatsResponse> => {
  return get(`/fishing/${year}/`);
};
