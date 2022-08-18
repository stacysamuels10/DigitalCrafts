import React from "react";

const validateEmail = () => {};

const FormComp = (props) => {
  const validateInput = (props, e) => {
    e.preventDefault();
    let validEmail =
      /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (validEmail.test(props.formData.email)) {
      props.setSubmitData({
        ...props.submitData,
        email: props.formData.email,
      });
    } else {
      alert("not valid email");
    }
    // write name validation name is greater than 5 characters
    // if (props.formData.firstName.length > 2) {
    //   props.setSubmitData({
    //     ...props.submitData,
    //     firstName: props.formData.firstName,
    //   });
    // } else {
    //   alert("Please enter a name with at least 3 characters");
    // }
    // write name validation name is greater than 5 characters
    if (props.formData.lastName.length > 2) {
      props.setSubmitData({
        ...props.submitData,
        lastName: props.formData.lastName,
      });
    } else {
      alert("Please enter a name with at least 3 characters");
    }
    // const specialChars = /[~`!@#$%&*+=';/{}|:<>?()_]/;
    // const capitalLetter = /[ABCDEFGHIJKLMNOPQRSTUVWXYZ]/;
    // const lowercaseLetter = /[abcdefghijklmnopqrstuvwxyz]/;
    // const number = /[123456780]/;
    // if (
    //   props.formData.password.length > 8 &&
    //   specialChars.test(props.formData.password) &&
    //   capitalLetter.test(props.formData.password) &&
    //   lowercaseLetter.test(props.formData.password) &&
    //   number.test(props.formData.password)
    // ) {
    //   props.setSubmitData({
    //     ...props.submitData,
    //     password: props.formData.password,
    //   });
    // }
  };
  return (
    <div>
      <button>Connect with Facebook</button>
      <button>Connect with Google</button>
      <p>Or sign up by Email</p>
      <form onSubmit={(e) => validateInput(props, e)}>
        <input
          name="firstName"
          value={props.formData.firstName}
          onChange={(e) =>
            props.setFormData({
              ...props.formData,
              [e.target.name]: e.target.value,
            })
          }
          placeholder="First Name"
          type="text"
        />
        <input
          name="lastName"
          value={props.formData.lastName}
          onChange={(e) =>
            props.setFormData({
              ...props.formData,
              [e.target.name]: e.target.value,
            })
          }
          placeholder="Last Name"
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
          placeholder="Email"
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
          type="password"
          placeholder="Password"
        />
        <input type="submit" value="Create Account" />
      </form>
      <p>
        By creating an account, you agree to our{" "}
        <a href="/TermsAndConds">Terms & Conditions</a>
      </p>
    </div>
  );
};

export default FormComp;
