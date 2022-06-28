console.log(document);

//document.
//getElementById
const button1 = parseInt(document.getElementById("button1").innerText);
const button2 = parseInt(document.getElementById("button2").innerText);
const calculate = document.getElementById("calculate");
//making a button that has a function
//listener is more encompassing
//addition.addEventListener("click", (howdy) => console.log(howdy));
//addEventListener("click", (e) => console.log(e)); almost everything
// the element
// addition.onclick = () => console.log("I was clicked") event
//addition.onclick = () => console.log("I was clicked");

const addition = document.getElementById("addition");

const calculate = () => {};

const sum = (total) => {
  console.log("this is the sum", total);
};
addition.onclick = sum;
calculate.onclick = calculate;
const buttons = document.getElementsByTagName("button");
for (const button of buttons) {
  console.log(button.innerText);
}
