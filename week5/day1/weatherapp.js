//enter zip
//get temp
const API_KEY = "44c139c6aab3ee37e9df0bde2b0ab1b6";

//https://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid={API key}
const input = document.querySelector("#input");
const submit = document.getElementById("submit");
const container = document.querySelector(".container");
const weather = document.querySelector(".weather");
const bgimage = document.querySelector(".bg-image");

const searchWeather = async () => {
  const input = document.getElementById("zip-code").value;
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${input},us&units=imperial&appid=${API_KEY}`;
  const weatherData = await fetch(url);
  const json = await weatherData.json();
  const background = (document.body.style.backgroundImage =
    "url(./backgrounds/" + json.weather[0].icon + ".jpg)");
  const stuff = document.createElement("div");
  stuff.classList = "stuff";
  weather.append(stuff);
  console.log(json);
  if (json.main.temp > 70) {
    const Jacket = document.createElement("p");
    Jacket.innerText = "No, you do not need a jacket";
    stuff.append(Jacket);
  }
  if (json.main.temp < 70 && json.main.temp > 55) {
    const Jacket = document.createElement("p");
    Jacket.innerText = "Bring a jacket just in case";
    stuff.append(Jacket);
  }
  if (json.main.temp < 55) {
    const Jacket = document.createElement("p");
    Jacket.innerText = "Skip the jacket. Straight to parka";
    stuff.append(Jacket);
  }
  const icon = document.createElement("img");
  const iconimg = json.weather[0].icon;
  icon.src = `http://openweathermap.org/img/wn/${iconimg}@2x.png`;
  stuff.append(icon);
  const city = document.createElement("h5");
  city.innerText = json.name;
  stuff.append(city);
  const showTemp = document.createElement("p");
  showTemp.innerText = `the temperature is ${Math.round(json.main.temp)}`;
  stuff.append(showTemp);
  const date = document.createElement("h5");
  d = new Date();
  date.innerText = d.toDateString();
  stuff.append(date);
  const feelsLike = document.createElement("p");
  feelsLike.innerText = `feels like ${Math.round(json.main.feels_like)}`;
  stuff.append(feelsLike);
  const weatherCondition = document.createElement("p");
  weatherCondition.innerText = `the current weather is ${json.weather[0].description}`;
  stuff.append(weatherCondition);
  const humidity = document.createElement("p");
  humidity.innerText = `the current humidity is ${json.main.humidity}%`;
  stuff.append(humidity);
  const windSpeed = document.createElement("p");
  windSpeed.innerText = `the current windspeed is ${json.wind.speed} knots`;
  stuff.append(windSpeed);
  const cloudiness = document.createElement("p");
  cloudiness.innerText = `the current cloudiness is ${json.clouds.all}%`;
  stuff.append(cloudiness);
};

submit.onclick = () => {
  weather.innerHTML = null;
  bgimage.innerHTML = null;
  searchWeather();
};
//needs city or zip code
