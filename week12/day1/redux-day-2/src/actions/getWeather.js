import { SET_WEATHER } from "../action-types/weatherActionTypes";

export const getWeather = async (dispatch, location) => {
  const url = `https://api.openweathermap.org/data/2.5/weather?zip=${location}&appid=44c139c6aab3ee37e9df0bde2b0ab1b6&units=imperial`;
  const weatherJson = await fetch(url);
  const json = await weatherJson.json();
  dispatch({ type: "SET_WEATHER", payload: json });
};

export const setSearch = async (dispatch, text) => {
  dispatch({ type: "SET_LOCATION", payload: text });
};
