import request from "request-promise-native";
import { BlogPostListParams, BlogPostList } from "../types/Blog";

console.log(process.env.NODE_ENV);
const baseUrl =
  process.env.NODE_ENV === "production"
    ? `${window.location.origin}/api`
    : "http://127.0.0.1:8000/api";

interface ApiInterface {
  listPosts: (params: BlogPostListParams) => Promise<BlogPostList>;
}

class Api implements ApiInterface {
  async listPosts(params: BlogPostListParams): Promise<BlogPostList> {
    return this.get(`/blog?page=${params.page}`);
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
    console.log(response);
    if (parseJson) {
      return JSON.parse(response);
    }
    return response;
  }
}

const api = new Api();

export default api;
