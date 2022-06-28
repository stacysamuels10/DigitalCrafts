let listOfOrders = [];
let moreCoffee = "";
let pourAmount = 0;

function prepCoffeeOrder() {
  var cupSize = window.prompt("What size coffee do you want? sm, med,lg");
  var strength = window.prompt(
    "What kind of strength do you want? normal, strong"
  );
  let order = {
    size: cupSize,
    caffiene: strength,
  };
  listOfOrders.push(order);
  return listOfOrders;
}

prepCoffeeOrder();

// function calcCoffeeGrind(listOfOrders) {
//   let grindAmount = 0;
//   let pourAmount = 0;

//   for (let index = 0; index < array.length; index++) {
//     const element = array[index];

//   }
//   {
//     order = _pj_a[_pj_c];

//     if (order["size"] === "sm") {
//       if (order["caffiene"] === "normal") {
//         grindAmount = grindAmount + 21;
//         pourAmount = pourAmount + 345;
//       }

//       if (order["caffiene"] === "strong") {
//         grindAmount = grindAmount + 23;
//         pourAmount = pourAmount + 345;
//       }
//     }

//     if (order["size"] === "med") {
//       if (order["caffiene"] === "normal") {
//         grindAmount = grindAmount + 28;
//         pourAmount = pourAmount + 450;
//       }

//       if (order["caffiene"] === "strong") {
//         grindAmount = grindAmount + 30;
//         pourAmount = pourAmount + 450;
//       }
//     }

//     if (order["size"] === "lg") {
//       if (order["caffiene"] === "normal") {
//         grindAmount = grindAmount + 33;
//         pourAmount = pourAmount + 525;
//       }

//       if (order["caffiene"] === "strong") {
//         grindAmount = grindAmount + 35;
//         pourAmount = pourAmount + 525;
//       }
//     }
//   }

//   console.log(`
// You will need to grind ${grindAmount} grams of coffee.
// Your first bloom pour will be ${grindAmount * 2} grams of hot water.
// Wait 45 - 60 seconds
// Your next pour will be up to ${pourAmount / 2} grams of hot water.
// Your final pour will be up to ${pourAmount} grams of hot water.
// Let the water turn to delicious bean water and enjoy!
// `);
// }

// while (moreCoffee.lower() !== "n") {
//   prepCoffeeOrder();
//   moreCoffee = input("Want more coffee? Y/N \n");
// }

// calcCoffeeGrind(listOfOrders);
