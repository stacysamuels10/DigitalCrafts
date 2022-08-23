import React from "react";
import { useAppDispatch } from "../app/hooks";
import { ProductDetail } from "../reducers/rootReducer";

const Product = (props: ProductDetail): JSX.Element => {
  const dispatch = useAppDispatch();
  const addToCart = (dispatch: any, productToBeAdded: ProductDetail) => {
    dispatch({ type: "ADD_TO_CART", payload: productToBeAdded });
  };
  return (
    <div>
      <h1>{props.description}</h1>
      <h1>{props.price}</h1>
      <button onClick={() => addToCart(dispatch, props)}>Add to Cart</button>
    </div>
  );
};

export default Product;
