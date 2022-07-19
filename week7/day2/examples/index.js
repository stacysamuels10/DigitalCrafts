import express from "express";
import es6Renderer from "express-es6-template-engine";
const app = express();
const PORT = 3030;

app.engine("html", es6Renderer);
app.set("views", "templates");
app.set("view engine", "html");

app.get("/", (req, res) => {
  // res.send("Hello from Express!");
  res.render("home");
});

app.get("/about", (req, res) => {
  res.render("about");
});

app.post("/home", (req, res) => {
  res.send("Hello from Express!");
});

app.listen(PORT, console.log(`lsitening on port ${PORT}`));
