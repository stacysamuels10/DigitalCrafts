import React from "react";
import { useAppSelector } from "../app/hooks";
import { createClient } from "@supabase/supabase-js";
const supabaseUrl = "https://mxakcphctxajogkuteth.supabase.co";
const supabaseAnonKey = "";
const supabase = createClient(supabaseUrl, supabaseAnonKey);

const Cart = (): JSX.Element => {
  const cart = useAppSelector((state) => state.cart);

  const sendToDatabase = async () => {
    const { data, error } = await supabase
      .from("ProductsDatabase")
      .insert([{ name: "Stacy", items: cart }]);
    console.log("data", data);
    console.log("error", error);
  };

  return (
    <div>
      <button onClick={sendToDatabase}>Complete Order</button>
      {cart.map((item) => {
        return (
          <>
            <h1>{item.price}</h1>
            <h1>{item.description}</h1>
          </>
        );
      })}
    </div>
  );
};

export default Cart;
