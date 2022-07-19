import express from "express";
import es6Renderer from "express-es6-template-engine";
const app = express();
const PORT = 3030;

app.engine("html", es6Renderer);
app.set("views", "templates");
app.set("view engine", "html");

app.get("/", (req, res) => {
  const todoItems = [
    { task: "Wash The Dishes" },
    { task: "Pay Off DC Loan" },
    { task: "Send 2 million job applications" },
    { task: "Message Rayleigh and ask her for Algo Help" },
    { task: "Ask Alyson why Joe has too many Dad jokes" },
    { task: "Try my best at 10 sum and realize that pain is horrible." },
    { task: "Figure out why I have more crypto than I do common sense." },
    { task: "Fill up the car with way too expensive gas" },
    { task: "Ask Blke for advice on which room is the best to work in" },
    { task: "Realize West is leaving us so that he can surf all day." },
  ];
  res.render("home", {
    locals: {
      todoItems: todoItems,
    },
  });
});

app.listen(PORT, console.log(`lsitening on port ${PORT}`));
