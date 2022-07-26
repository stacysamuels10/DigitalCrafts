//const { Pets } = require("../../models");
const express = require("express");
const router = express.Router();

//create
router.post("/create_pets", (req, res) => {
  res.send("create_pets");
});
//read
router.get("/get_pets", (req, res) => {
  //get the index.html page and view an html
  //that says pets
  res.render("index");
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
