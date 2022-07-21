const express = require("express");
const { User } = require("./models/user");
const app = express();
const port = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/users", async (req, res) => {
  //user final all using async await
  const users = await User.findAll();
});

app.listen(port, () => console.log(`Listening on port ${port}`));
