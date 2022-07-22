const express = require("express");
const { User } = require("./models");
const app = express();
const port = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

//read all users
app.get("/users", async (req, res) => {
  //user final all using async await
  console.log(User);
  const users = await User.findAll();
  res.send(users);
});

//read a user by id
app.get("/users/:id", async (req, res) => {
  //user final all using async await
  const id = req.params.id;
  const user = await User.findByPk(id);
  res.send(user);
  //   console.log(User);
  //   const users = await User.findAll();
  //   res.send(users);
});
app.listen(port, () => console.log(`Listening on port ${port}`));
