// D R Y
//Dont Repeat Yourself
//if you keep repeating, make it a function

let count = 0;
count = 1;
count = 2;
count = 3;

//use keyword function to define a function (the old way)
function incrementNumber(number) {
  return number++;
  //function body
  //dont have to return unless you want to
}

incrementNumber();
