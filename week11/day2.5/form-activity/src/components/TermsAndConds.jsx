import React from "react";
import { useNavigate } from "react-router-dom";

const TermsAndConds = () => {
  const navigate = useNavigate();
  const navigateToSignUp = () => {
    navigate("/");
  };
  return (
    <div>
      <h1>
        By signing up you agree that Joe will never be a better coder than Blke.
      </h1>
      <button onClick={navigateToSignUp}>Return to Sign Up</button>
    </div>
  );
};

export default TermsAndConds;
