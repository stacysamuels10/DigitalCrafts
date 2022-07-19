require("dotenv").config();

const express = require("express");
const { createClient } = require("@supabase/supabase-js");
const supabase = createClient(process.env.SUPABASE_URL, process.env.API_KEY);
const app = express();
const PORT = process.env.PORT || 3030;

app.post("/", (req, res) => {});

app.listen(PORT, console.log(`listening on port ${PORT}`));
