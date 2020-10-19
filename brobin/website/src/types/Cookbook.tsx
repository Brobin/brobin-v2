import { Dayjs } from "dayjs";

type Ingredient = {
  name: string;
};

type IngredientAmount = {
  ingredient: Ingredient;
  amount: string;
};

type Step = {
  text: string;
};

export type Recipe = {
  title: string;
  created: Dayjs;
  updated: Dayjs;
  slug: string;
  notes: string;
  prep_time: number;
  cook_time: number;
  ingredients: Array<IngredientAmount>;
  steps: Array<Step>;
};

export type RecipeListResponse = {
  count: number;
  next: string;
  previous: string;
  results: Array<Recipe>;
};
