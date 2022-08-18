import React from "react";

export default function Prop5(props) {
  return (
    <div>
      Prop5
      {props.houses.map((house) => (
        <h1>{house.name}</h1>
      ))}
      <h1>{props.owner.name}</h1>
    </div>
  );
}
