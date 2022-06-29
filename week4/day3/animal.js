const dropdown = document.getElementById("animal-farm");
const animalNoiseContainer = document.querySelector(".animal-noise");
const animalChoice = (emoji) => {
  animalNoiseContainer.innerHTML = null;
  //figure out how to create elements
  const animalNoise = document.createElement("p");
  //figure out how to attach those elements to the web pages
  if (emoji === "🐷") {
    console.log("oink oink");
    animalNoise.innerText = "oink oink";
  } else if (emoji === "🐱") {
    console.log("meow");
    animalNoise.innerText = "meow";
  } else if (emoji === "🐶") {
    animalNoise.innerText = "woof";
    console.log("woof");
  } else {
    console.log("cluck cluck");
    animalNoise.innerText = "cluck cluck";
  }
  animalNoiseContainer.append(animalNoise);
};
dropdown.onchange = (event) => animalChoice(event.target.value);

//console.log(dropdown.children[0].value);
// const pig = dropdown.children[0].value;
