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

interface ApiInterface {
  listPosts: (params: BlogPostListParams) => Promise<BlogPostListResponse>;
  getPost: (params: BlogPostDetailParams) => Promise<BlogPost>;
  getBlogSidebar: () => Promise<BlogSidebarResponse>;
  listRecipes: () => Promise<RecipeListResponse>;
  getRecipe: (params: RecipeDetailParams) => Promise<Recipe>;
  getFishingStats: () => Promise<FishingStatsResponse>;
  getFishingYearStats: (year: number) => Promise<FishingYearStatsResponse>;
}

class Api implements ApiInterface {
  async listPosts(params: BlogPostListParams): Promise<BlogPostListResponse> {
    if (params.category) {
      return this.get(`/blog/${params.category}/?page=${params.page}`);
    } else if (params.year) {
      return this.get(`/blog/archive/${params.year}/`);
    } else if (params.query) {
      return this.get(`/blog/search/?page${params.page}&query=${params.query}`);
    }
    return this.get(`/blog/?page=${params.page}`);
  }

  async getPost(params: BlogPostDetailParams): Promise<BlogPost> {
    return this.get(`/blog/${params.year}/${params.month}/${params.slug}/`);
  }

  async getBlogSidebar(): Promise<BlogSidebarResponse> {
    return this.get("/blog/sidebar/");
  }

  async listRecipes(): Promise<RecipeListResponse> {
    return this.get(`/cookbook/`);
  }

  async getRecipe(params: RecipeDetailParams): Promise<Recipe> {
    return this.get(`/cookbook/${params.slug}`);
  }

  async getFishingStats(): Promise<FishingStatsResponse> {
    return this.get(`/fishing/`);
  }

  async getFishingYearStats(year: number): Promise<FishingYearStatsResponse> {
    return this.get(`/fishing/${year}/`);
  }

  async post(route: string, params = {}) {
    const requestOptions = {
      url: `${baseUrl}${route}`,
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(params),
    };
    const response = await request(requestOptions);
    return JSON.parse(response);
  }

  async get(route: string, parseJson = true) {
    const requestOptions = {
      url: `${baseUrl}${route}`,
      method: "GET",
      headers: { "Content-Type": "application/json" },
    };
    const response = await request(requestOptions);
    if (parseJson) {
      return JSON.parse(response);
    }
    return response;
  }
}

const api = new Api();

export default api;
