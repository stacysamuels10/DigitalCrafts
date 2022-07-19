require("dotenv").config();

const express = require("express");
const app = express();
const PORT = process.envPORT || 3030;

app.listen(PORT, console.log(`listening on port ${PORT}`));
