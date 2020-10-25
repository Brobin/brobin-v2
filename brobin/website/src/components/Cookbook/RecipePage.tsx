import {
  Card,
  CardContent,
  Container,
  createStyles,
  Grid,
  LinearProgress,
  makeStyles,
  Theme,
  Typography,
} from "@material-ui/core";
import React, { useState } from "react";
import { RouteComponentProps } from "react-router-dom";
import { Recipe, RecipeDetailParams } from "../../types/Cookbook";
import * as api from "../../utils/api";
import { useLoader } from "../../utils/hooks";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    container: {
      padding: theme.spacing(3),
    },
  })
);

const RecipePage: React.FC<RouteComponentProps<RecipeDetailParams>> = ({
  match,
}) => {
  const slug = match.params.slug;
  const classes = useStyles();

  const [recipe, setRecipe] = useState<Recipe>();

  const loadRecipe = async (): Promise<void> => {
    const thisRecipe = await api.getRecipe({ slug });
    setRecipe(thisRecipe);
  };

  const { loaded } = useLoader(loadRecipe);

  return !loaded || !recipe ? (
    <LinearProgress color="secondary" />
  ) : (
    <Container>
      <div className={classes.container}>
        <Typography variant="h5">{recipe.title}</Typography>
        <p>{recipe.notes}</p>
        <Grid container>
          <Grid item sm={5}>
            <Card>
              <CardContent>
                <ul>
                  {recipe.ingredients.map((ingredientAmount) => {
                    return (
                      <li>
                        {ingredientAmount.ingredient.name}{" "}
                        {ingredientAmount.amount}
                      </li>
                    );
                  })}
                </ul>
              </CardContent>
            </Card>
          </Grid>
          <Grid item sm={7}>
            <ol>
              {recipe.steps.map((step) => {
                return <li>{step.text}</li>;
              })}
            </ol>
          </Grid>
        </Grid>
      </div>
    </Container>
  );
};

export default RecipePage;
