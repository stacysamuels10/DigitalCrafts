const { Clients } = require("../../models");
const express = require("express");
const router = express.Router();

const bcrypt = require("bcrypt");

router.get("/all_users", async (req, res) => {
  const usersToGet = await Clients.findAll();
  res.send(usersToGet);
});

module.exports = router;

router.get("/by_id/:id", async (req, res) => {
  const { id } = req.params;
  const usersToGet = await Clients.findAll({
    where: {
      id: id,
    },
  });
  res.send(usersToGet);
});

router.post("/create_user", async (req, res) => {
  const { username, password } = req.body;
  try {
    const salt = await bcrypt.genSalt(5);
    const hashedPassword = await bcrypt.hash(password, salt);
    const encryptedUser = {
      username: username,
      password: hashedPassword,
      createdAt: new Date(),
      updatedAt: new Date(),
    };

    const createUser = await Clients.create(encryptedUser);
    res.send(createUser);
  } catch (error) {
    console.log(error);
  }
});

router.post("/login", async (req, res) => {
  const { username, password } = req.body;
  try {
    //find user based on username in our database
    const findUser = await Clients.findOne({
      where: {
        username: username,
      },
    });

    const userWeFound = findUser.dataValues;
    console.log(userWeFound.password);
    const validated = await bcrypt.compare(password, userWeFound.password);
    console.log(validated);
    if (!findUser) {
      res
        .status(400)
        .send(
          "that user did not exist in our database, did you get your username correct?"
        );
    } else {
      res.status(200).send(findUser.dataValues);
    }
  } catch (error) {
    res.send(error);
  }
});

router.put("/change_password", async (req, res) => {
  const { username, password } = req.body;
  try {
    //find user based on username in our database
    const findUser = await Clients.findOne({
      where: {
        username: username,
      },
    });
    if (!findUser) {
      res
        .status(400)
        .send(
          "that user did not exist in our database, did you get your username correct?"
        );
    } else {
      const salt = await bcrypt.genSalt(5);
      const hashedPassword = await bcrypt.hash(password, salt);
      const updatedUser = findUser.update({
        username: username,
        password: hashedPassword,
        updatedAt: new Date(),
      });
    }
  } catch (error) {
    res.send(error);
  }
});

router.delete("/delete_user", async (req, res) => {
  const { username, password } = req.body;
  try {
    //find user based on username in our database
    const findUser = await Clients.findOne({
      where: {
        username: username,
      },
    });
    if (!findUser) {
      res
        .status(400)
        .send(
          "that user did not exist in our database, did you get your username correct?"
        );
    } else {
      const updatedUser = findUser.destroy();
    }
  } catch (error) {
    res.send(error);
  }
});
