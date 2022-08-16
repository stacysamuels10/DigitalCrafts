import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import About from "./components/About";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Product from "./components/Product";
import ProductCard from "./components/ProductCard";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <BrowserRouter>
    <Navbar></Navbar>
    <Routes>
      <Route path="/" element={<App />}></Route>
      <Route path="/about" element={<About />}></Route>
      <Route path="/product" element={<Product />}>
        <Route path=":productId" element={<ProductCard />}></Route>
      </Route>
    </Routes>
  </BrowserRouter>
);
