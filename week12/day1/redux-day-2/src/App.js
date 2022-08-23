import "./App.css";
import WeatherContainer from "./components/WeatherContainer";
import WeatherSearch from "./components/WeatherSearch";

function App() {
  return (
    <div className="App">
      <WeatherSearch />
      <WeatherContainer />
    </div>
  );
}

export default App;
