const express = require("express");
const app = express();
const bcrypt = require("bcrypt");
const PORT = 3030;

app.use(express.json());
//request object
//req.body as long as you have app.use(express.json());
//{
// "username" : "stacy.samuels",
// "password" : "hello123"
// }
//req.body.password -> "hello123"

app.post("/create_user", async (req, res) => {
  const { password } = req.body;
  try {
    const salt = await bcrypt.genSalt(20);
    console.log(salt);
  } catch (error) {}
  console.log(req.body);
  res.send("create user");
});

app.listen(PORT, console.log(`listening on port ${PORT}`));
