import React from "react";

export default function WeatherCard({ zipCode }) {
  const { name, weather, main } = zipCode;
  const icon = `http://openweathermap.org/img/wn/${weather[0]?.icon}@2x.png`;
  return (
    <>
      {weather[0] && (
        <div className="weatherCard">
          <div className="leftSideCard">
            <p className="weather">{weather[0].description}</p>
            <div className="extraInfo">
              <div className="feels">
                <p className="small-label">Feels Like</p>
                <p className="large-label">{Math.round(main?.feels_like)}</p>
              </div>
              <div className="humid">
                <p className="small-label">Humidity</p>
                <p className="large-label">{Math.round(main?.humidity)}</p>
              </div>
            </div>
            <h3 className="name">{name}</h3>
          </div>
          <div className="rideSideCard">
            <h1 className="temp">{`${Math.round(main?.temp)} F`}</h1>
            <img src={icon} alt="" />
          </div>
        </div>
      )}
    </>
  );
}
