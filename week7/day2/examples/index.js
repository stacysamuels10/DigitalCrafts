import express from "express";
import es6Renderer from "express-es6-template-engine";
const app = express();
const PORT = 3030;

app.engine("html", es6Renderer);
app.set("views", "templates");
app.set("view engine", "html");
app.use(express.static("public"));
//this line lets us use local pathing for our html and css

app.get("/", (req, res) => {
  // res.send("Hello from Express!");
  const user = { name: "Stacy" };
  res.render("home", {
    locals: {
      user: user,
      teacher: "Joe",
      students: ["Amanda", "Carlos"],
    },
  });
});

app.get("/about", (req, res) => {
  res.render("about");
});

app.post("/home", (req, res) => {
  console.log(req.body.message);
  res.json(req.body.message);
});

app.listen(PORT, console.log(`lsitening on port ${PORT}`));
