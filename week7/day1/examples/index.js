import { createInterface } from "readline";
import { readFile } from "node:fs";
import { writeFile } from "node:fs";

let readline = createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline.question("File Name: ", function (filename) {
  readline.close();
  readFile(
    `/Users/stacysamuels/Desktop/digitalCrafts/week7/day1/examples/${filename}`,
    "utf8",
    (err, message) => {
      if (err) {
        return console.log(err);
      }
      console.log(message.toUpperCase());
    }
  );
});
