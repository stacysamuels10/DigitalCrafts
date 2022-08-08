"use strict";
const fizzBuzz = (num) => {
    if (num % 3 === 0 && num % 5 === 0) {
        return "fizzbuzz";
    }
    else if (num % 3 === 0) {
        return "fizz";
    }
    else if (num % 5 === 0) {
        return "buzz";
    }
    else {
        return "not valid";
    }
};
console.log(fizzBuzz(3));
console.log(fizzBuzz(5));
console.log(fizzBuzz(15));
console.log(fizzBuzz(1));
