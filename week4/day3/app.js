//ternary operation ?
// donst data = iftruth ? do this : do this if falsy
//makes a variable a little bit dynamic
const admin = "joe";
const username = admin === "joe" ? "jwfraiser" : "rrozier";
console.log(username);

//const loggenIn = username === "joe"
// AND opertor &&
const loggenIn = username === "joe" && "jwfraiser";

//OR operator
// ||

const permittedToStay = loggenIn || "child";

const array1 = ["andrea", "amanda", "jason"];
const array2 = ["west", "rahmin", "rahmin's mother"];
//const students = array1.concat(array2);
//spread operator

const students = [...array1, ...array2];
console.log(students);

const notANumber = "1";
console.log(typeof +notANumber);

students.forEach((element) => {
  console.log(element.toUpperCase());
});
//if you break up your logic into more than one line, you have to return
const upperCasedStudents = students.map((student) => student.toUpperCase());
console.log(upperCasedStudents);

const googleEmployee = {
    name : "Sundar Pichai"
    status: "ceo"
    salary: "1 billion dollars"
}

const noogleEmployee = {
    name : "Carlos Silva"
    status: "noogler"
    salary: "not 1 billion"
}

console.log(googleEmployee.height)