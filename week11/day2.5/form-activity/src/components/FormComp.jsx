import React from "react";
import { useState } from "react";

const FormComp = (props) => {
  const validateInput = (props, e) => {
    e.preventDefault();
    switch (props.formData.email) {
      case props.formData.email:
        let validEmail =
          /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (validEmail.test(props.formData.email)) {
          props.setFormData({ ...props.formData, email: props.formData.email });
        } else {
          alert("not valid email");
        }
        break;
      // case props.name:
      //   // write name validation name is greater than 5 characters
      //   if (props.name.length > 5) {
      //     console.log("success");
      //   } else {
      //     console.log("error");
      //   }
      //   break;

      // default:
      //   break;
    }
  };
  return (
    <div>
      <form onSubmit={(e) => validateInput(props, e)}>
        <input
          name="name"
          value={props.formData.name}
          onChange={(e) =>
            props.setFormData({
              ...props.formData,
              [e.target.name]: e.target.value,
            })
          }
          placeholder="name"
          type="text"
        />
        <input
          name="email"
          value={props.formData.email}
          onChange={(e) =>
            props.setFormData({
              ...props.formData,
              [e.target.name]: e.target.value,
            })
          }
          placeholder="email"
          type="text"
        />
        <input
          value={props.formData.password}
          name="password"
          onChange={(e) =>
            props.setFormData({
              ...props.formData,
              [e.target.name]: e.target.value,
            })
          }
          type="text"
          placeholder="password"
        />
        <input
          name="address"
          value={props.formData.address}
          onChange={(e) =>
            props.setFormData({
              ...props.formData,
              [e.target.name]: e.target.value,
            })
          }
          type="text"
          placeholder="address"
        />
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
};

export default FormComp;
