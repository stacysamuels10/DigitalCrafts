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
        <h6>Weather App</h6>
        <div className="inputandsearch">
          <input
            type="text"
            placeholder="Enter US Zip Code"
            onChange={(e) =>
              dispatch({ type: "SET_LOCATION", payload: e.target.value })
            }
          />
          <button onClick={() => getWeather()}>🔎</button>
        </div>
      </div>
      <div className="weatherCard">
        <h4 className="title">Today's Weather</h4>
        <img
          className="icon"
          src={`http://openweathermap.org/img/wn/${weather?.weather[0]?.icon}@2x.png`}
          alt=""
        />
        <div className="mainweather">
          <h1>{`${Math.round(weather?.main?.temp)}\u00B0 F`}</h1>
          <p className="weatherCond">
            {weather?.weather[0]?.description.charAt(0).toUpperCase() +
              weather?.weather[0]?.description.slice(1).toLowerCase()}
          </p>
          <p className="city">{`📍 ${weather?.name}`}</p>
        </div>
        <div className="extrainfo">
          <div className="feels">
            <p className="large-label">{`${Math.round(
              weather?.main?.feels_like
            )}\u00B0 F`}</p>
            <p className="small-label">🌡️ Feels like</p>
          </div>
          <div className="humid">
            <p className="large-label">{`${Math.round(
              weather?.main?.humidity
            )}%`}</p>
            <p className="small-label">💧 Humidity</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
