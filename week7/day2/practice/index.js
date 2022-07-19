import express from "express";
import es6Renderer from "express-es6-template-engine";
const app = express();
const PORT = 3030;

const es6Renderer = require("express-es6-template-engine");
app.engine("html", es6Renderer);
app.set("views", "templates");
app.set("view engine", "html");
