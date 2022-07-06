//enter zip
//get temp
const API_KEY = "44c139c6aab3ee37e9df0bde2b0ab1b6";

//https://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid={API key}
const input = document.querySelector("#input");
const submit = document.getElementById("submit");
const container = document.querySelector(".container");
const weather = document.querySelector(".weather");
const bgimage = document.querySelector(".bg-image");
const stuff = document.querySelector(".stuff");
const Jackets = document.getElementById("jacket");
const icons = document.getElementById("icon");
const citys = document.getElementById("city");
const temp = document.getElementById("temp");
const dates = document.getElementById("date");
const feels = document.getElementById("feelsLike");
const currentWeather = document.getElementById("current-weather");
const humid = document.getElementById("humidity");
const winds = document.getElementById("windspeed");
const cloudy = document.getElementById("cloudiness");
const h = document.querySelectorAll("h");

const searchWeather = async () => {
  const input = document.getElementById("zip-code").value;
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${input},us&units=imperial&appid=${API_KEY}`;
  const weatherData = await fetch(url);
  const json = await weatherData.json();
  const background = (document.body.style.backgroundImage =
    "url(./backgrounds/" + json.weather[0].icon + ".jpg)");
  console.log(json);

  if (json.main.temp > 70) {
    const Jacket = document.createElement("p");
    Jacket.innerText = "No, you do not need a jacket";
    Jacket.classList = "grid";
    Jackets.append(Jacket);
    stuff.append(Jackets);
  }
  if (json.main.temp < 70 && json.main.temp > 55) {
    const Jacket = document.createElement("p");
    Jacket.innerText = "Bring a jacket just in case";
    Jacket.classList = "grid";
    Jackets.append(Jacket);
    stuff.append(Jackets);
  }
  if (json.main.temp < 55) {
    const Jacket = document.createElement("p");
    Jacket.innerText = "Skip the jacket. Straight to parka";
    Jacket.classList = "grid";
    Jackets.append(Jacket);
    stuff.append(Jackets);
  }

  const icon = document.createElement("img");
  const iconimg = json.weather[0].icon;
  icon.src = `http://openweathermap.org/img/wn/${iconimg}@2x.png`;
  icon.classList = "grid";
  icons.append(icon);
  stuff.append(icons);

  const cityH = document.createElement("h5");
  cityH.innerText = "City";
  citys.append(cityH);
  const city = document.createElement("p");
  city.innerText = json.name;
  city.classList = "grid";
  citys.append(city);
  stuff.append(citys);

  const tempH = document.createElement("h5");
  tempH.innerText = "Temperature";
  temp.append(tempH);
  const showTemp = document.createElement("p");
  showTemp.innerText = Math.round(json.main.temp);
  showTemp.classList = "grid";
  temp.append(showTemp);
  stuff.append(temp);

  const dateH = document.createElement("h5");
  dateH.innerText = "Date";
  dates.append(dateH);
  const date = document.createElement("h5");
  d = new Date();
  date.innerText = d.toDateString();
  date.classList = "grid";
  dates.append(date);
  stuff.append(dates);

  const feelsLikeH = document.createElement("h5");
  feelsLikeH.innerText = "Feels Like";
  feels.append(feelsLikeH);
  const feelsLike = document.createElement("p");
  feelsLike.innerText = Math.round(json.main.feels_like);
  feelsLike.classList = "grid";
  feels.append(feelsLike);
  stuff.append(feels);

  const weatherH = document.createElement("h5");
  weatherH.innerText = "Current Weather";
  currentWeather.append(weatherH);
  const weatherCondition = document.createElement("p");
  weatherCondition.innerText = json.weather[0].description;
  weatherCondition.classList = "grid";
  currentWeather.append(weatherCondition);
  stuff.append(currentWeather);

  const humidityH = document.createElement("h5");
  humidityH.innerText = "Humidity";
  humid.append(humidityH);
  const humidity = document.createElement("p");
  humidity.innerText = `${json.main.humidity}%`;
  humidity.classList = "grid";
  humid.append(humidity);
  stuff.append(humid);

  const windH = document.createElement("h5");
  windH.innerText = "Wind Speed";
  winds.append(windH);
  const windSpeed = document.createElement("p");
  windSpeed.innerText = `${json.wind.speed} knots`;
  windSpeed.classList = "grid";
  winds.append(windSpeed);
  stuff.append(winds);

  const cloudH = document.createElement("h5");
  cloudH.innerText = "Cloudiness";
  cloudy.append(cloudH);
  const cloudiness = document.createElement("p");
  cloudiness.innerText = `${json.clouds.all}%`;
  cloudiness.classList = "grid";
  cloudy.append(cloudiness);
  stuff.append(cloudy);
};

submit.onclick = () => {
  Jackets.innerHTML = null;
  icons.innerHTML = null;
  citys.innerHTML = null;
  temp.innerHTML = null;
  dates.innerHTML = null;
  feels.innerHTML = null;
  currentWeather.innerHTML = null;
  humid.innerHTML = null;
  winds.innerHTML = null;
  cloudy.innerHTML = null;
  searchWeather();
};
//needs city or zip code
