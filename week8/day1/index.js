const express = require("express");
const { Clients } = require("./models");
const app = express();
const es6Renderer = require("express-es6-template-engine");
const bcrypt = require("bcrypt");
const PORT = 3030;
const router = express.Router();

app.use(express.json());
const userRoutes = require("./server/user");
const restaurantsRoutes = require("./server/restuarants");

app.use("/user", userRoutes);
app.use("/restaurants", restaurantsRoutes);
app.use(express.static("public"));
app.engine("html", es6Renderer);
app.set("views", "./public/views");
app.set("view engine", "html");

app.get("/", function (req, res) {
  res.render("index");
});

app.listen(PORT, console.log(`listening on port ${PORT}`));
