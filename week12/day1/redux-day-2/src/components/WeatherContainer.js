import React from "react";
import { useSelector } from "react-redux";
import WeatherCard from "./WeatherCard";
import "../App.css";

export default function WeatherContainer() {
  const weather = useSelector((state) => state.weather);
  return (
    <div className="weatherContainer">
      {weather?.map((zipCode) => (
        <WeatherCard zipCode={zipCode} />
      ))}
    </div>
  );
}
