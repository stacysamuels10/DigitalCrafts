//what is a promise
//promise is an asynchronous action
//an actian you take and you wait on an expected result
// it will either be what you wanted or not
// resolve or reject

//async
function getCoffee(type) {
  //we look for the type of coffee in our database
  console.log("you walk up and grab a cup of joe");
}
// async function, async action, promise
// const oliviasCofee = async getTypeOfCoffee()
// getCoffee(oliviasCofee);

const getCoffeePromise = new Promise((resolve, reject) => {
  const coffee = "blonde roast";
  //type of, takes an anonymous function and receives a resolve and reject
  if (coffee === "black") {
    resolve("I have your black coffee");
  } else {
    reject("I do not have black coffee");
  }
});

console.log(getCoffeePromise);
//this returns a promise, cant do anything with a promise
