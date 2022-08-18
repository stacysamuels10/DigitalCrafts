import React from "react";

const Output = (props) => {
  return (
    <div>
      <h1>Account Info</h1>
      <h4>First Name: {props.submitData.firstName}</h4>
      <h4>Last Name: {props.submitData.lastName}</h4>
      <h4>Email: {props.submitData.email}</h4>
    </div>
  );
};

export default Output;
