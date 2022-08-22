import "./App.css";
import { useSelector, useDispatch } from "react-redux";

function App() {
  const dispatch = useDispatch();
  const weather = useSelector((state) => state.weather);

  return (
    <div className="App">
      <h1>Weather App</h1>
      <h1>{weather.conditions}</h1>
      <button onClick={() => dispatch({ type: "SET_WEATHER" })}>
        Set Weather
      </button>
    </div>
  );
}

export default App;
