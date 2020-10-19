import React from "react";
import get from "lodash.get";
import { useLocation } from "react-router-dom";
import { Error400, Error401, Error403, Error404, Error500 } from "./Error";

const ErrorBoundary: React.FC = ({ children }) => {
  const location = useLocation();

  switch (get(location.state, "errorStatusCode")) {
    case 400:
      return <Error400 />;
    case 401:
      return <Error401 />;
    case 403:
      return <Error403 />;
    case 404:
      return <Error404 />;
    case 500:
      return <Error500 />;
    default:
      return <>{children}</>;
  }
};

export default ErrorBoundary;
