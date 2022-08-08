const fizzBuzz = (num: number): string => {
  if (num % 3 === 0 && num % 5 === 0) {
    return "fizzbuzz";
  }
  if (num % 3 === 0) {
    return "fizz";
  }
  if (num % 5 === 0) {
    return "buzz";
  } else {
    return "not valid";
  }
};

console.log(fizzBuzz(3));
console.log(fizzBuzz(5));
console.log(fizzBuzz(15));
console.log(fizzBuzz(1));
