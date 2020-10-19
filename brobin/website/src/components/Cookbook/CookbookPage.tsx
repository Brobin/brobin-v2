import { Container, Grid, LinearProgress } from "@material-ui/core";
import React, { useState } from "react";
import { Recipe, RecipeListResponse } from "../../types/Cookbook";
import api from "../../utils/api";
import { useLoader } from "../../utils/hooks";
import RecipePreview from "./RecipePreview";

const CookbookPage: React.FC = () => {
  const [recipes, setRecipes] = useState<Array<Recipe>>([]);

  const loadRecipes = async () => {
    const data: RecipeListResponse = await api.listRecipes();
    setRecipes(data.results);
  };

  const { loaded } = useLoader(loadRecipes);

  return !loaded ? (
    <LinearProgress color="secondary" />
  ) : (
    <Container>
      <Grid container>
        <Grid item sm={8}>
          {recipes.map((recipe) => {
            return <RecipePreview recipe={recipe} />;
          })}
        </Grid>
      </Grid>
    </Container>
  );
};

export default CookbookPage;
