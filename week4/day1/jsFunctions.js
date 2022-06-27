// D R Y
//Dont Repeat Yourself
//if you keep repeating, make it a function

let count = 0;
count = 1;
count = 2;
count = 3;

//use keyword function to define a function (the old way)
function incrementNumber(number = 0) {
  let total = number + 1;
  return total;
  //function body
  //dont have to return unless you want to
}
//if you get NaN, you need to write code that can handle a number
//false-y values in js "" '' ``, string length of zero, null, undefined, NaN, document.all, false
console.log(incrementNumber(12));

//ES5 way of writing a function
//arrow function
//defining a function as a variable
//make const a const variable, they should not change
const arrowIncrement = (number) => {
  let total = number + 1;
  return total;
};

const writeMyName = (name) => {
  console.log(name);
};

function multiply(number) {
  return number * 10;
}

const pointlessFunction = () => {
  return null;
};

const writeNameBackwards = (name) => {
  return name.reverse();
};
