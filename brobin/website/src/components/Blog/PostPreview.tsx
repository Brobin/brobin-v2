import React from 'react'
import dayjs from 'dayjs'
import { Typography } from '@material-ui/core';
import { BlogPost } from '../../types/Blog';

interface PostPreviewProps {
    post: BlogPost
}


const PostPreview: React.FC<PostPreviewProps> = props => (
  <>
    <Typography variant="h6">{props.post.title}</Typography>
    <Typography variant="body1">{dayjs(props.post.created).format('MMMM D, YYYY h:mm A')}</Typography>
    <Typography variant="body2">{props.post.preview}</Typography>
  </>
);

export default PostPreview;
