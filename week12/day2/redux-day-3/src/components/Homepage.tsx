import React from "react";
import Products from "./Products";
import Cart from "./Cart";

const Homepage = (): JSX.Element => {
  return (
    <div className="homepage">
      <div className="products">
        <Products />
      </div>
      <Cart />
    </div>
  );
};

export default Homepage;
