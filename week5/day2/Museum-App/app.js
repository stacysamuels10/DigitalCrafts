const submit = document.getElementById("submit");
let selected = "";
const imagespot = document.getElementById("image");
const hints = document.getElementById("hints");
const hintButton = document.getElementById("hint-department");
const solution = document.getElementById("solution");
const container = document.querySelectorAll("container");

const findSelected = () => {
  const element = document.getElementsByName("region");
  for (let i = 0; i < element.length; i++) {
    if (element[i].checked) {
      selected = element[i].value;
      return selected;
    }
  }
};

const searchMuseum = async (selected) => {
  const url = `https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&hasImages=true&isOnView=true&q=${selected}`;
  const museumData = await fetch(url);
  const json = await museumData.json();
  const item = json.objectIDs;
  let random = item[Math.floor(Math.random() * item.length)];
  const url2 = `https://collectionapi.metmuseum.org/public/collection/v1/objects/${random}`;
  const objectArray = await fetch(url2);
  const randomArtwork = await objectArray.json();
  console.log(randomArtwork);
  const hintbtn = document.createElement("button");
  hintbtn.innerHTML = "Extra Hint?";
  hintButton.append(hintbtn);
  const image = document.createElement("img");
  image.src = randomArtwork.primaryImage;
  imagespot.append(image);
  const hint1 = document.createElement("p");
  hint1.innerText = randomArtwork.objectDate;
  hints.append(hint1);
  const hint2 = document.createElement("p");
  hint2.innerText = randomArtwork.medium;
  hints.append(hint2);
  hintbtn.onclick = () => {
    const hint3 = document.createElement("p");
    hint3.innerText = `You can find this in the ${randomArtwork.department} department`;
    hints.append(hint3);
    hintbtn.setAttribute("disabled", "disabled");
  };
  const solutionbtn = document.createElement("button");
  solutionbtn.innerHTML = "Check to see if you're right?";
  solution.append(solutionbtn);
  solutionbtn.onclick = () => {
    const artist = document.createElement("p");
    artist.innerText = `The artist is ${randomArtwork.artistDisplayName} and the artwork is called ${randomArtwork.title}`;
    solution.append(artist);
    solutionbtn.setAttribute("disabled", "disabled");
  };
};

submit.onclick = () => {
  solution.innerHTML = null;
  hints.innerHTML = null;
  hintButton.innerHTML = null;
  imagespot.innerHTML = null;
  findSelected();
  searchMuseum(selected);
};
