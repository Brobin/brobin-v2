import { Container, Typography } from "@material-ui/core";
import React, { useState } from "react";
import { FishingStatsResponse } from "../../types/Fishing";
import api from "../../utils/api";
import { useLoader } from "../../utils/hooks";

const StatsPage: React.FC = () => {
  const [graphs, setGraphs] = useState<FishingStatsResponse>();

  const loadStats = async () => {
    const data = await api.getFishingStats();
    setGraphs(data);
  };

  const { loaded } = useLoader(loadStats);

  return (
    <Container>
      <Typography variant="h4" style={{ textAlign: "center" }}>
        Brown Family Fishing Trip
      </Typography>
      <>
        {loaded && graphs && (
          <>
            <figure
              dangerouslySetInnerHTML={{
                __html: graphs.bar,
              }}
            />
            <figure
              dangerouslySetInnerHTML={{
                __html: graphs.line,
              }}
            />
            <figure
              dangerouslySetInnerHTML={{
                __html: graphs.punchcard,
              }}
            />
            <figure
              dangerouslySetInnerHTML={{
                __html: graphs.scatter,
              }}
            />
          </>
        )}
      </>
    </Container>
  );
};

export default StatsPage;
