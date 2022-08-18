import { useEffect, useState } from "react";
import { Routes, Route, useNavigate } from "react-router-dom";
import MovieContainer from "./components/MovieContainer";
import About from "./components/About";
import NavBar from "./components/NavBar";
import MovieInfo from "./components/MovieInfo";
import "./App.css";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";

function App() {
  const state = {
    movies: [
      {
        Title: "Guardians of the Galaxy Vol. 2",
        Year: "2017",
        Rated: "PG-13",
        Released: "05 May 2017",
        Runtime: "136 min",
        Genre: "Action, Adventure, Comedy",
        Director: "James Gunn",
        Writer: "James Gunn, Dan Abnett, Andy Lanning",
        Actors: "Chris Pratt, Zoe Saldana, Dave Bautista",
        Plot: "The Guardians struggle to keep together as a team while dealing with their personal family issues, notably Star-Lord's encounter with his father the ambitious celestial being Ego.",
        Language: "English",
        Country: "United States",
        Awards: "Nominated for 1 Oscar. 15 wins & 59 nominations total",
        Poster:
          "https://m.media-amazon.com/images/M/MV5BNjM0NTc0NzItM2FlYS00YzEwLWE0YmUtNTA2ZWIzODc2OTgxXkEyXkFqcGdeQXVyNTgwNzIyNzg@._V1_SX300.jpg",
        Ratings: [
          {
            Source: "Internet Movie Database",
            Value: "7.6/10",
          },
          {
            Source: "Rotten Tomatoes",
            Value: "85%",
          },
          {
            Source: "Metacritic",
            Value: "67/100",
          },
        ],
        Metascore: "67",
        imdbRating: "7.6",
        imdbVotes: "665,736",
        imdbID: "tt3896198",
        Type: "movie",
        DVD: "22 Aug 2017",
        BoxOffice: "$389,813,101",
        Production: "N/A",
        Website: "N/A",
        Response: "True",
      },
      {
        Title: "testing",
        Year: "2004",
        Rated: "PG-13",
        Released: "05 May 2017",
        Runtime: "100 min",
        Genre: "Action, Adventure",
        Director: "Joe Gunn",
        Writer: "James Gunn, Dan Abnett, Andy Lanning",
        Actors: "Chris Pratt, Zoe Saldana, Dave Bautista",
        Plot: "The Guardians struggle to keep together as a team while dealing with their personal family issues, notably Star-Lord's encounter with his father the ambitious celestial being Ego.",
        Language: "English",
        Country: "United States",
        Awards: "Nominated for 1 Oscar. 15 wins & 59 nominations total",
        Poster:
          "https://m.media-amazon.com/images/M/MV5BNjM0NTc0NzItM2FlYS00YzEwLWE0YmUtNTA2ZWIzODc2OTgxXkEyXkFqcGdeQXVyNTgwNzIyNzg@._V1_SX300.jpg",
        Ratings: [
          {
            Source: "Internet Movie Database",
            Value: "7.6/10",
          },
          {
            Source: "Rotten Tomatoes",
            Value: "85%",
          },
          {
            Source: "Metacritic",
            Value: "67/100",
          },
        ],
        Metascore: "99",
        imdbRating: "10.0",
        imdbVotes: "665,736",
        imdbID: "tt3896198X",
        Type: "movie",
        DVD: "22 Aug 2017",
        BoxOffice: "$389,813,101",
        Production: "N/A",
        Website: "N/A",
        Response: "True",
      },
    ],
  };
  const [movies, setMovies] = useState([]);
  const [currentMovie, setCurrentMovie] = useState({});
  const [inputField, setInputField] = useState("");

  const navigate = useNavigate();
  const getMovies = async () => {
    try {
      const result = await fetch(
        `http://www.omdbapi.com/?apikey=a53478d9&s=${inputField}`
      );
      const json = await result.json();
      setMovies(json.Search);
      navigate("/MovieContainer");
    } catch (error) {
      alert("Movies cannot be found");
    }
  };

  return (
    <div className="App">
      <NavBar></NavBar>
      <div className="container">
        <h1>Movie Search</h1>
        <TextField
          label="Search"
          variant="standard"
          type="text"
          name="search"
          id="search"
          size="small"
          onChange={(e) => setInputField(e.target.value)}
        />
        <Button variant="outlined" onClick={getMovies} size="small">
          Find Your Movie
        </Button>
      </div>
      <Routes>
        <Route path="/About" element={<About />}></Route>
        <Route
          path="/MovieContainer"
          element={
            <MovieContainer movies={movies} setCurrentMovie={setCurrentMovie} />
          }
        ></Route>
        <Route
          path="/MovieInfo"
          element={
            <MovieInfo
              currentMovie={currentMovie}
              setCurrentMovie={setCurrentMovie}
            />
          }
        ></Route>
      </Routes>
    </div>
  );
}

export default App;
