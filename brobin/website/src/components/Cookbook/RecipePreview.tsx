import React from "react";
import {
  Card,
  CardContent,
  createStyles,
  makeStyles,
  Theme,
  Typography,
} from "@material-ui/core";
import Link from "../Link";
import { Recipe } from "../../types/Cookbook";

interface RecipePreviewProps {
  recipe: Recipe;
}

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    card: {
      margin: theme.spacing(3),
      marginRight: 0,
    },
  })
);

const RecipePreview: React.FC<RecipePreviewProps> = (props) => {
  const classes = useStyles();
  return (
    <Card className={classes.card}>
      <CardContent>
        <Typography variant="h6">
          <Link to="">{props.recipe.title}</Link>
        </Typography>
        <Typography variant="body2">{props.recipe.notes}</Typography>
      </CardContent>
    </Card>
  );
};

export default RecipePreview;
