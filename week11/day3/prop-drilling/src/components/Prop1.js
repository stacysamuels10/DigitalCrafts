import React from "react";
import Prop2 from "./Prop2";

export default function Prop1(props) {
  return (
    <div>
      Prop1
      <Prop2 houses={props.houses} owner={props.owner} />
    </div>
  );
}
