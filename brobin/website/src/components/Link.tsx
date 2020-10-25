import React from "react";
import { Link as RouterLink } from "react-router-dom";
import { Link as MuiLink } from "@material-ui/core";

interface LinkProps {
  to: string;
  children: React.ReactNode;
}

const Link: React.FC<LinkProps> = (props) => (
  <MuiLink color="secondary" to={props.to} component={RouterLink}>
    {props.children}
  </MuiLink>
);

export default Link;
