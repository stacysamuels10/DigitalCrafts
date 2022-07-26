const { Restuarants } = require("../../models");
const express = require("express");
const router = express.Router();

//create 1 or more resutrant
//read 1 by id
//read 1 by name
//read 1 resturant by address

//update the name of restaurant
//update the address of restaurant

//delete 1 by id
//delete 1 by name
router.post("/create_restaurant", async (req, res) => {
  const { name, address, reviewScore } = req.body;
  try {
    const newRestaurant = {
      name: name,
      address: address,
      reviewScore: reviewScore,
      createdAt: new Date(),
      updatedAt: new Date(),
    };
    const createRestaurant = await Restuarants.create(newRestaurant);
    res.send(createRestaurant);
  } catch (error) {
    console.log(error);
  }
});

router.get("/by_id/:id", async (req, res) => {
  const { id } = req.params;
  const restaurantToGet = await Restuarants.findAll({
    where: {
      id: id,
    },
  });
  res.send(restaurantToGet);
});

router.get("/by_name", async (req, res) => {
  const { name } = req.body;
  const restaurantToGet = await Restuarants.findAll({
    where: {
      name: name,
    },
  });
  res.send(restaurantToGet);
});

router.get("/by_address", async (req, res) => {
  const { address } = req.body;
  const restaurantToGet = await Restuarants.findAll({
    where: {
      address: address,
    },
  });
  res.send(restaurantToGet);
});

router.put("/update_name", async (req, res) => {
  const { name } = req.body;
  try {
    //find user based on username in our database
    const findUser = await Restuarants.findOne({
      where: {
        name: name,
      },
    });
    if (!findUser) {
      res
        .status(400)
        .send(
          "that Restaurant did not exist in our database, did you get your name correct?"
        );
    } else {
      const { newName } = req.body;
      const updatedUser = findUser.update({
        name: newName,
        updatedAt: new Date(),
      });
    }
  } catch (error) {
    res.send(error);
  }
});

router.put("/update_address", async (req, res) => {
  const { name } = req.body;
  try {
    //find user based on username in our database
    const findUser = await Restuarants.findOne({
      where: {
        name: name,
      },
    });
    if (!findUser) {
      res
        .status(400)
        .send(
          "that Restaurant did not exist in our database, did you get your name correct?"
        );
    } else {
      const { address } = req.body;
      const updatedUser = findUser.update({
        name: name,
        address: address,
        updatedAt: new Date(),
      });
    }
  } catch (error) {
    res.send(error);
  }
});

router.delete("/delete_restaurant", async (req, res) => {
  const { name } = req.body;
  try {
    //find user based on username in our database
    const findUser = await Restuarants.findOne({
      where: {
        name: name,
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

router.delete("/delete_restaurant_id/:id", async (req, res) => {
  const { id } = req.params;
  try {
    //find user based on username in our database
    const findUser = await Restuarants.findOne({
      where: {
        id: id,
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

module.exports = router;
