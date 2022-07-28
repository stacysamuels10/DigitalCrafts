const express = require("express");
const { Users, Sessions } = require("./models");
const app = express();
const models = require("./models");
const es6Renderer = require("express-es6-template-engine");
const bcrypt = require("bcrypt");
const session = require("express-session");
const cookieParser = require("cookie-parser");
const SequelizeStore = require("connect-session-sequelize")(session.Store);
const store = new SequelizeStore({
  db: models.sequelize,
});
const PORT = 3030;

//middleware
app.use(express.json());
app.engine("html", es6Renderer);
app.set("views", "views");
app.set("view engine", "html");
app.use(express.json());
app.use(cookieParser());
app.use(
  session({
    secret: "secret",
    resave: false,
    saveUninitialized: true,
    store: store,
  })
);
store.sync();

app.post("/login", async (req, res) => {
  const user = await Users.findOne({
    where: {
      username: req.body.username,
      password: req.body.password,
    },
  });
  if (user) {
    req.session.user = user;
    console.log(req.session.user);
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
const checkLogin = async (req, res, next) => {
  const sessionValid = await Sessions.findOne({
    where: {
      sid: req.session.sid,
    },
  });
  if (sessionValid) {
    next();
  } else {
    res.json({
      message: "Login Required",
    });
  }
};

app.get("/home", checkLogin, (req, res) => {
  console.log(req.session);
  res.render("index", { locals: { name: req.session.user } });
});

app.post("/delete_all_secrets", checkLogin, async (req, res) => {
  res.send("You must be legit, we deleted everything");
});

app.listen(PORT, () => {
  console.log(`listening on port ${PORT}`);
});
