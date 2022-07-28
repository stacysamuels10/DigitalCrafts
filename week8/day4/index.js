const express = require("express");
const { Users } = require("./models");
const app = express();
const es6Renderer = require("express-es6-template-engine");
const bcrypt = require("bcrypt");
const session = require("express-session");
const cookieParser = require("cookie-parser");
const PORT = 3030;

//middleware
app.use(cookieParser());
app.use(
  session({
    secret: "secret",
    resave: false,
    saveUninitialized: true,
    cookie: {
      maxAge: 2592000000,
      secure: false,
    },
  })
);

app.use(express.json());

app.post("/login", async (req, res) => {
  const user = await Users.findOne({
    where: {
      username: req.body.username,
      password: req.body.password,
    },
  });
  if (user) {
    req.session.user = user;
    res.json({
      message: "Login Success",
      user: user,
    });
  } else {
    res.json({
      message: "Login Failed",
    });
  }
});

//function used on where your routes are
const checkLogin = (req, res, next) => {
  if (req.session.user) {
    next();
  } else {
    res.json({
      message: "Login Required",
    });
  }
};

app.post("/delete_all_secrets", checkLogin, async (req, res) => {
  res.send("You must be legit, we deleted everything");
});

app.listen(PORT, () => {
  console.log(`listening on port ${PORT}`);
});
