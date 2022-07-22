const express = require("express");
const { User, Longboard, Order } = require("../database/models");
const app = express();
const PORT = 3031;

//crud

app.listen(PORT, console.log(`listening on port ${PORT}`));
