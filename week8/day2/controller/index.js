const express = require("express");
const app = express();
const cors = require("cors");
const PORT = 3030;
const petsRoutes = require("./routes/pets");

//middleware
app.use(express.json());
app.use(cors());
app.use("/pets", petsRoutes);
//

app.listen(PORT, console.log(`listening on Port ${PORT}`));
