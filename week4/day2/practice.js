console.log(document);

//document.
//getElementById
//making a button that has a function
//listener is more encompassing
//addition.addEventListener("click", (howdy) => console.log(howdy));
//addEventListener("click", (e) => console.log(e)); almost everything
// the element
// addition.onclick = () => console.log("I was clicked") event
//addition.onclick = () => console.log("I was clicked");

const numbersToCalc = [];
let answer = "";

const calculate = () => {};

const sum = (total) => {
  console.log("this is the sum", total);
};

const getButtonValue = (buttonInnerText) => {
  if (buttonInnerText.id === "addition") {
    let mathSign = buttonInnerText.innerText;
    numbersToCalc.push(mathSign);
  } else {
    const innerTextToInt = parseInt(buttonInnerText.innerText);
    numbersToCalc.push(innerTextToInt);
  }

  console.log(numbersToCalc);
};

const doMaff = () => {
  const firstVal = numbersToCalc[0];
  const mathSign = numbersToCalc[1];
  const secondVal = numbersToCalc[2];
  if (mathSign === "+") {
    console.log(firstVal + secondVal);
    answer = firstVal + secondVal;
    input.value = answer;
  }
};
const input = document.getElementById("textbox");
const button1 = document.getElementById("button1");
const button2 = document.getElementById("button2");
const calc = document.getElementById("calculate");
const addition = document.getElementById("addition");

calc.onclick = doMaff;
button1.onclick = (e) => getButtonValue(e.target);
button2.onclick = (e) => getButtonValue(e.target);
addition.onclick = (e) => getButtonValue(e.target);
const bigAnswer = document.createElement("h1");
bigAnswer.innerText = "Cowboy";
container.append(bigAnswer);
