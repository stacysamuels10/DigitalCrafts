//enter zip
//get temp
const API_KEY = "44c139c6aab3ee37e9df0bde2b0ab1b6";

//https://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid={API key}
const input = document.querySelector("#input");
const submit = document.getElementById("submit");
const container = document.querySelector(".container");
const stuff = document.querySelector(".stuff");

const searchWeather = async () => {
  const input = document.getElementById("zip-code").value;
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${input},us&units=imperial&appid=${API_KEY}`;
  console.log(url);
  const weatherData = await fetch(url);
  const json = await weatherData.json();
  console.log(json);
  const showTemp = document.createElement("p");
  showTemp.innerText = json.main.temp;
  stuff.append("the temperature is ", showTemp);
  const city = document.createElement("h5");
  city.innerText = json.name;
  stuff.append(city);
  const icon = document.createElement("img");
  const iconimg = json.weather[0].icon;
  icon.src = `http://openweathermap.org/img/wn/${iconimg}@2x.png`;
  stuff.append(icon);
};

submit.onclick = () => {
  stuff.innerHTML = null;
  searchWeather();
};
//needs city or zip code
