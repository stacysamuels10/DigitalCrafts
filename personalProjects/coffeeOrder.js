const container = document.getElementsByClassName("container");
const submit = document.getElementById("submit");
const sizes = document.querySelectorAll(".name");

const sizeSelection = () => {
  for (let index = 0; index < sizes.length; index++) {
    console.log("hello");
  }
};

submit.onclick = sizeSelection;
