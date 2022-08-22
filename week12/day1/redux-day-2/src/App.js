import "./App.css";
import { useSelector, useDispatch } from "react-redux";

function App() {
  const dispatch = useDispatch();
  const weather = useSelector((state) => state.weather);
  const user = useSelector((state) => state.user);
  const location = useSelector((state) => state.location);
  const getWeather = async () => {
    const url = `https://api.openweathermap.org/data/2.5/weather?zip=${location}&appid=44c139c6aab3ee37e9df0bde2b0ab1b6&units=imperial
`;
    const weatherJson = await fetch(url);
    const json = await weatherJson.json();
    dispatch({ type: "SET_WEATHER", payload: json });
  };
  return (
    <div className="App">
      <div className="search">
        <h1>Weather App</h1>
        <input
          type="text"
          placeholder="Enter US Zip Code"
          onChange={(e) =>
            dispatch({ type: "SET_LOCATION", payload: e.target.value })
          }
        />
        <button onClick={() => getWeather()}>🔎</button>
      </div>
      <div className="weatherCard">
        <h4 className="title">Today's Weather</h4>
        <img
          className="icon"
          src={`http://openweathermap.org/img/wn/${weather?.weather[0]?.icon}@2x.png`}
          alt={weather?.weather[0]?.description}
        />
        <div className="mainweather">
          <p className="weatherCond">{weather?.weather[0]?.description}</p>
          <p className="city">{`📍 ${weather?.name}`}</p>
          <p>{`${Math.round(weather?.main?.temp)}\u00B0 F`}</p>
        </div>
        <div className="extrainfo">
          <p>{`🌡️ Feels like: ${Math.round(
            weather?.main?.feels_like
          )}\u00B0 F`}</p>
          <p>{`💧 Humidity: ${Math.round(weather?.main?.humidity)}%`}</p>
        </div>
      </div>
    </div>
  );
}

export default App;
