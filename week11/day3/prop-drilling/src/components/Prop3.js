import React from "react";
import Prop4 from "./Prop4";

export default function Prop3(props) {
  return (
    <div>
      Prop3
      <Prop4 houses={props.houses} owner={props.owner} />
    </div>
  );
}
