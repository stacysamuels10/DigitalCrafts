require("dotenv").config();

const express = require("express");
const { createClient } = require("@supabase/supabase-js");
const supabase = createClient(process.env.SUPABASE_URL, process.env.API_KEY);
const app = express();
const PORT = process.env.PORT || 3030;

app.use(express.json());

app.post("/create_student", async (req, res) => {
  console.log(req.body);
  const { data, error } = await supabase.from("web-06-22").insert([req.body]);
  if (data) {
    res.send(data);
  }
  if (error) {
    res.send(error);
  }
});

app.listen(PORT, console.log(`listening on port ${PORT}`));
