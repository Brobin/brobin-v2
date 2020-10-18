import React from "react";
import dayjs from "dayjs";
import {
  Card,
  CardContent,
  createStyles,
  makeStyles,
  Theme,
  Typography,
} from "@material-ui/core";
import PostLink from "./PostLink";
import { BlogPost } from "../../types/Blog";

interface PostPreviewProps {
  post: BlogPost;
}

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    card: {
      margin: theme.spacing(3),
    },
  })
);

const PostPreview: React.FC<PostPreviewProps> = (props) => {
  const classes = useStyles();

  return (
    <Card className={classes.card}>
      <CardContent>
        <Typography variant="h6">
          <PostLink post={props.post} />
        </Typography>
        <Typography variant="body1">
          {dayjs(props.post.created).format("MMMM D, YYYY h:mm A")}
        </Typography>
        <Typography variant="body2">{props.post.preview}</Typography>
      </CardContent>
    </Card>
  );
};

export default PostPreview;
