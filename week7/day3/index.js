// default expess app is set to port 3000
const express = require("express");
const creds = require("./server/databaseConnection");
const app = express();
app.use(express.json());
const port = 3000;

// READ ALL ANIME DATA
app.get("/", (req, res) => {
  console.log(creds);
  creds.query("SELECT * FROM movie", (err, result) => {
    if (err) {
      console.log(err);
      res.sendStatus(500);
    } else {
      res.json(result.rows);
    }
  });
});
app.post("/create_movie", (req, res) => {
  console.log(req.body);
  creds.query(
    "INSERT INTO movie (movie_name, genre, year_created, ranking) VALUES ($1, $2, $3, $4)",
    [
      req.body.movie_name,
      req.body.genre,
      req.body.year_created,
      req.body.ranking,
    ],
    (err, result) => {
      if (err) {
        console.log(err);
        res.status(500).send(err);
      } else {
        res.status(200).send(result);
      }
    }
  );
});

app.post("/update_movie", (req, res) => {
  creds.query(
    "UPDATE movie SET year_created=$1 WHERE id = $2",
    [req.body.year_created, req.body.id],
    (err, result) => {
      if (err) {
        res.status(500).send(err);
      } else {
        res.status(200).send(result);
      }
    }
  );
});

app.delete("/delete_movie", (req, res) => {
  creds.query("DELETE FROM movie WHERE id=$1", [req.body.id], (err, result) => {
    if (err) {
      res.status(500).send(err);
    } else {
      res.status(200).send(result);
    }
  });
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
