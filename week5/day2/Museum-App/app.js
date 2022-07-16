const submit = document.getElementById("submit");
let selected = "";
const imagespot = document.getElementById("image");
const hints = document.getElementById("hints");
const solution = document.getElementById("solution");
const container = document.querySelectorAll("container");
const loading = document.getElementById("loading");

const findSelected = () => {
  const element = document.getElementsByName("region");
  for (let i = 0; i < element.length; i++) {
    if (element[i].checked) {
      selected = element[i].value;
      return selected;
    }
  }
};

const loadNewPage = () => {
  loading.append(imagespot, hints, solution);
  imagespot.innerHTML = null;
  hints.innerHTML = null;
  solution.innerHTML = null;
};

const searchMuseum = async (selected) => {
  loadNewPage();
  const url = `https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&hasImages=true&isOnView=true&q=${selected}`;
  const museumData = await fetch(url);
  const json = await museumData.json();
  const item = json.objectIDs;
  let random = item[Math.floor(Math.random() * item.length)];
  const url2 = `https://collectionapi.metmuseum.org/public/collection/v1/objects/${random}`;
  const objectArray = await fetch(url2);
  const randomArtwork = await objectArray.json();
  const image = document.createElement("img");
  image.src = randomArtwork.primaryImage;
  imagespot.append(image);
  const hintHeader = document.createElement("h3");
  hintHeader.innerText = "HINTS:";
  const hintbtn = document.createElement("button");
  hintbtn.innerHTML = "Extra Hint?";
  hintbtn.id = "hint1";
  const hint1 = document.createElement("p");
  hint1.innerText = `Estimated Date Created: ${randomArtwork.objectDate}`;
  const hint2 = document.createElement("p");
  hint2.innerText = `Medium(material): ${randomArtwork.medium}`;
  hints.append(hintHeader, hintbtn, hint1, hint2);
  hintbtn.onclick = () => {
    const hint3 = document.createElement("p");
    hint3.innerText = `You can find this in the ${randomArtwork.department} department`;
    hints.append(hint3);
    hintbtn.setAttribute("disabled", "disabled");
  };
  const solutionHeader = document.createElement("h3");
  solutionHeader.innerText = "SOLUTION:";
  const solutionbtn = document.createElement("button");
  solutionbtn.innerHTML = "Check to see if you're right?";
  solutionbtn.id = "solution1";
  solution.append(solutionHeader, solutionbtn);
  solutionbtn.onclick = () => {
    const artist = document.createElement("p");
    artist.innerText = `The artwork is called ${randomArtwork.title}`;
    solution.append(artist);
    solutionbtn.setAttribute("disabled", "disabled");
    const link = document.createElement("a");
    link.innerHTML = "Click Here to Learn More";
    link.href = randomArtwork.objectURL;
    solution.append(link);
  };
};

submit.onclick = () => {
  loading.innerHTML = null;
  findSelected();
  searchMuseum(selected);
};

window.onload = () => {
  loading.innerHTML = null;
};
