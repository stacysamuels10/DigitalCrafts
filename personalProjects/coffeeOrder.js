const container = document.getElementsByClassName("container");
const submit = document.getElementById("submit");
const sizes = document.querySelectorAll(".name");
const strength = document.querySelectorAll(".strength");

const sizeSelection = () => {
  for (i = 0; i < sizes.length; i++) {
    if (sizes[i].checked == true) {
      console.log(sizes[i].value, "this is the size");
    }
  }
};

const caffieneSelection = () => {
  for (i = 0; i < strength.length; i++) {
    if (strength[i].checked == true) {
      console.log(strength[i].value, "this is the strength");
    }
  }
};

submit.onclick = () => {
  sizeSelection();
  caffieneSelection();
};
