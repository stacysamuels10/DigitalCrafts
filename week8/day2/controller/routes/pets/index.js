const { Pets } = require("../../../sequelize/models");
const express = require("express");
const router = express.Router();

//create
router.post("/create_pets", (req, res) => {
  res.send("create_pets");
});
//read
router.get("/get_pets", async (req, res) => {
  //get the index.html page and view an html
  //that says pets
  const PetsIWant = await Pets.findAll({});
  res.render("index", {
    locals: { title: PetsIWant },
  });
  //res.send("get pets");
});
//update
router.put("/update_pets", (req, res) => {
  res.send("update pets");
});
//destroy
router.delete("/destroy_pets", (req, res) => {
  res.send("destroy pets");
});
module.exports = router;
