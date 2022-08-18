import React from "react";
import { useEffect, useState } from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Typography from "@mui/material/Typography";

const MovieInfo = (currentMovie) => {
  const [moreInfo, setMoreInfo] = useState([]);
  useEffect(() => {
    const getCurrentMovieInfo = async () => {
      try {
        const result = await fetch(
          `http://www.omdbapi.com/?apikey=a53478d9&t=${currentMovie.currentMovie.Title}`
        );
        const json = await result.json();
        setMoreInfo(json);
      } catch (error) {
        alert("Movies cannot be found");
      }
    };
    getCurrentMovieInfo(currentMovie.currentMovie);
  }, []);

  return (
    <div>
      <Card>
        <CardMedia component="img" image={moreInfo.Poster} />
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            {moreInfo.Title}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Released: {moreInfo.Released}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Director: {moreInfo.Director}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Main Actors: {moreInfo.Actors}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            {moreInfo.Plot}
          </Typography>
        </CardContent>
      </Card>
    </div>
  );
};

export default MovieInfo;
