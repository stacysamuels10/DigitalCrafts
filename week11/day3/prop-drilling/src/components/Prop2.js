import React from "react";
import Prop3 from "./Prop3";

export default function Prop2(props) {
  return (
    <div>
      Prop2
      <Prop3 houses={props.houses} owner={props.owner} />
    </div>
  );
}
