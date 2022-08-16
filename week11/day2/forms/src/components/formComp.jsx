import React from "react";
import { useState } from "react";

const formComp = () => {
  const defaultForm = {
    name: "",
    password: "",
    address: "",
    email: "",
  };
  const [formData, setFormData] = useState(defaultForm);

  const validateInput = () => {
    switch (formData) {
      case formData.email:
        let validEmail =
          /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (validEmail.test(formData.email)) {
          setFormData({ ...formData, email: formData.email });
        } else {
          //not submitted
        }
        break;
      case "name":
        // write name validation name is greater than 5 characters
        setFormData({ ...formData, name: formData.name });
        break;

      default:
        break;
    }
  };
  return (
    <div>
      <form>
        <input
          name="name"
          value={formData.name}
          onChange={(e) =>
            setFormData({ ...formData, [e.target.name]: e.target.value })
          }
          placeholder="name"
          type="text"
        />
        <input
          name="email"
          value={formData.email}
          onChange={(e) =>
            setFormData({ ...formData, [e.target.name]: e.target.value })
          }
          placeholder="email"
          type="text"
        />
        <input
          value={formData.password}
          name="password"
          onChange={(e) =>
            setFormData({ ...formData, [e.target.name]: e.target.value })
          }
          type="text"
          placeholder="password"
        />
        <input
          name="address"
          value={formData.address}
          onChange={(e) =>
            setFormData({ ...formData, [e.target.name]: e.target.value })
          }
          type="text"
          placeholder="address"
        />
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
};

export default formComp;
