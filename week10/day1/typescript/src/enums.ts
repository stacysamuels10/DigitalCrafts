// enumerate

const enum Directions {
  up = 1,
  down = 1,
  left = 1,
  right = 1,
}

const right = Directions.right;
const left = Directions.left;

const enum TshirtSizes {
  Small = "s",
  Medium = "m",
  Large = "l",
}

if (TshirtSizes.Medium === "m") {
  console.log("medium shirt");
}
const joeSize = TshirtSizes.Small;
