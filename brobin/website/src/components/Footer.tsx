import React from "react";
import dayjs from "dayjs";
import {
  Box,
  Container,
  Grid,
  Link,
  makeStyles,
  Theme,
  Typography,
} from "@material-ui/core";
import LinkedInIcon from "@material-ui/icons/LinkedIn";
import FacebookIcon from "@material-ui/icons/Facebook";
import GitHubIcon from "@material-ui/icons/GitHub";
import TwitterIcon from "@material-ui/icons/Twitter";

const useStyles = makeStyles((theme: Theme) => ({
  footer: {
    width: "100%",
    color: theme.palette.grey.A100,
    backgroundColor: theme.palette.primary.main,
    padding: theme.spacing(3),
    marginTop: theme.spacing(3),
  },
  icon: {
    color: theme.palette.grey.A100,
    paddingRight: "10px",
    float: "right",
  },
}));

const Footer: React.FC = () => {
  const classes = useStyles();
  return (
    <Box component="div" className={classes.footer}>
      <Container>
        <Grid container>
          <Grid item sm={6}>
            <Typography variant="caption">
              &copy; 2013-{dayjs().format("YYYY")} Tobin Brown
            </Typography>
          </Grid>
          <Grid item sm={6} style={{ float: "right" }}>
            <Link
              href="https://www.linkedin.com/pub/tobin-brown/91/393/720"
              className={classes.icon}
            >
              <LinkedInIcon />
            </Link>
            <Link
              href="https://www.facebook.com/tobinjbrown"
              className={classes.icon}
            >
              <FacebookIcon />
            </Link>
            <Link
              href="https://twitter.com/RobinWithaT"
              className={classes.icon}
            >
              <TwitterIcon />
            </Link>
            <Link href="https://github.com/Brobin" className={classes.icon}>
              <GitHubIcon />
            </Link>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
};

export default Footer;
