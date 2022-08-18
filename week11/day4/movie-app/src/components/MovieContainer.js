import React from "react";
import MovieCard from "./MovieCard";

const MovieContainer = ({ movies, setCurrentMovie }) => {
  return (
    <div className="MovieContainer">
      <p>Let's find some movies!</p>
      {movies?.map((movie) => {
        return (
          <MovieCard
            movie={movie}
            key={movie.imdbID}
            setCurrentMovie={setCurrentMovie}
          />
        );
      })}
    </div>
  );
};

export default MovieContainer;

//this is where you map the data
