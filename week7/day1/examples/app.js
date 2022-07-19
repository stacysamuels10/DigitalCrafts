import express from "express";
const app = express();
const PORT = 3033;
app.use(express.json());
//route usually will have its http method on it
//it will always include in this order
//a req and a res
console.log("i'm outside the route");
app.get("/", (req, res) => {
  //inside of this function body
  console.log("im inside the route");
  res.send("this is the home page");
});

app.get("/benji", (req, res) => {
  res.send("lizard");
});

app.post("/beer", (req, res) => {
  res.send("beer");
});

app.post("/create_user", (req, res) => {
  console.log(req.body);
  res.send(`Created user ${req.body.discplayer}`);
});

//3 routes
//1 get, 2 post

import { say } from "cowsay";

app.get("/graze", (req, res) => {
  res.send(say({ text: "grazing in the browser" }));
});

app.post("/tongue", (req, res) => {
  res.send(
    say({
      text: `${req.body.text}`,
    })
  );
});

app.get("/hello", (req, res) => {
  res.send("Hello World");
});

app.listen(PORT, console.log(`listening on port ${PORT}`));
