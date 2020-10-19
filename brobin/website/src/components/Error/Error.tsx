import React from "react";
import { Container, Typography } from "@material-ui/core";

interface ErrorProps {
  code: number;
  message: string;
}

const Error: React.FC<ErrorProps> = ({ code, message }) => (
  <Container>
    <Typography variant="h1" style={{ textAlign: "center" }}>
      {code}
    </Typography>
    <Typography variant="h6" style={{ textAlign: "center" }}>
      {message}
    </Typography>
  </Container>
);

export const Error400: React.FC = () => (
  <Error code={404} message={"Bad Request"} />
);

export const Error401: React.FC = () => (
  <Error code={404} message={"Unauthorized"} />
);

export const Error403: React.FC = () => (
  <Error code={404} message={"Forbidden"} />
);

export const Error404: React.FC = () => (
  <Error code={404} message={"Page Not Found"} />
);

export const Error500: React.FC = () => (
  <Error code={500} message={"Internal Server Error"} />
);
