import "./App.css";
import MovieContainer from "./components/MovieContainer";

function App() {
  return (
    <div className="App">
      <h1>
        Movie App
        <MovieContainer />
      </h1>
    </div>
  );
}

export default App;
//App will be calling all of the other components
