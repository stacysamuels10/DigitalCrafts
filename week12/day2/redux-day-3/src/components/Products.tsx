import React from "react";
import { useAppSelector } from "../app/hooks";
import Product from "./Product";

const Products = (): JSX.Element => {
  const products = useAppSelector((state) => state.products);
  return (
    <div>
      {products.map((product) => (
        <Product {...product} />
      ))}
    </div>
  );
};

export default Products;
