import React from "react";
import { getWeather, setSearch } from "../actions/getWeather";
import { useDispatch, useSelector } from "react-redux";

export default function WeatherSearch() {
  const dispatch = useDispatch();
  const location = useSelector((state) => state.location);
  return (
    <div className="search">
      <input
        type="text"
        onChange={(e) => setSearch(dispatch, e.target.value)}
        placeholder="Enter your Zip Code"
      />
      <button
        className="searchbutton"
        onClick={() => getWeather(dispatch, location)}
      >
        Find Weather
      </button>
    </div>
  );
}
