"use strict";
// () => {}
//parameters, arguments, body, name, return value
const returnTwelve = () => {
    return 12;
};
const returnArrayOfNumbers = (num1, num2) => {
    return [num1, num2];
};
const parsePassword = (password) => {
    if (password) {
        return true;
    }
    return false;
};
const calcIncomeTax = (salary, state) => {
    if (state) {
        const total = salary * 1.3;
        return total * 1.2;
    }
    if (salary > 120000) {
        return salary * 1.3;
    }
    return salary * 1.25;
};
