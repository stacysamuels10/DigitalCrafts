function lvl5exercise1() {
  // Push the string "hello" into the array and return the array
  var arr = [1, "adam"];
  arr.push("hello");
  return arr;
}
//console.log(lvl5exercise1());

function lvl5exercise2() {
  // Remove the last element from the array and return the array
  var arr = [1, "adam"];
  arr.pop();
  return arr;
}
//console.log(lvl5exercise2());

function lvl5exercise3() {
  // Return the length of the array
  var arr = [1, "adam"];
  return arr.length;
}
//console.log(lvl5exercise3());

function lvl5exercise4() {
  // Return the index of item "adam" in the array
  var arr = [1, "adam"];
  return arr.indexOf("adam");
}
console.log(lvl5exercise4());

function lvl6exercise1(num) {
  // Return 'hello' if num is 1, 'world' if num is 2, otherwise return 'bye'
  // use a switch statement
  switch (num) {
    case 1:
      console.log("hello");
      break;
    case 2:
      console.log("world");
      break;
    default:
      console.log("bye");
      break;
  }
}
//lvl6exercise1(5);
function lvl6exercise2() {
  // Push 10 'hello' strings into the array using a for loop, then return it
  var array = [];
  for (let index = 0; index < 10; index++) {
    array.push("hello");
  }
  return array;
}
//console.log(lvl6exercise2());

function lvl6exercise3() {
  // Empty this array using a while loop and return it
  var arr = [
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
  ];
  while (arr.length > 0) {
    arr.pop();
  }
  return arr;
}
//console.log(lvl6exercise3());

// Write a function that takes a number as an input.
// Have it create an empty array and then push a string into the array as many
// times as the input number. If the input is anything other than a positive
// integer return an empty array
//
// Name the function "finalFunction"

const finalFunction = (num) => {
  arr = [];
  if (num > 0) {
    for (let index = 0; index < num; index++) {
      arr.push("hi");
    }
  } else {
    return arr;
  }
  return arr;
};

//console.log(finalFunction(-2));

const mul = (argument) => {
  array = [];
  for (let index = 0; index < argument; index++) {
    array.push();
  }
  return array;
};

//console.log(mul(2)(3)(4));
