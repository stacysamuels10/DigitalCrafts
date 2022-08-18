import React from "react";
import { useNavigate } from "react-router-dom";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Typography from "@mui/material/Typography";
import { Button, CardActionArea, CardActions } from "@mui/material";

const MovieCard = ({ movie, setCurrentMovie }) => {
  const navigate = useNavigate();
  const handleClick = () => {
    setCurrentMovie(movie);
    navigate("/MovieInfo");
  };

  return (
    <div>
      <Card sx={{ maxWidth: 200 }}>
        <CardMedia
          component="img"
          height="200px"
          width="200px"
          image={movie.Poster}
        />
        <CardContent>
          <Typography
            sx={{ maxWidth: 200 }}
            gutterBottom
            variant="p"
            component="div"
          >
            {movie.Title}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            {movie.Year}
          </Typography>
        </CardContent>

        <CardActions>
          <Button size="small" color="primary" onClick={handleClick}>
            Movie Info
          </Button>
        </CardActions>
      </Card>
    </div>
  );
};

export default MovieCard;
