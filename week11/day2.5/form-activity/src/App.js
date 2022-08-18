import "./App.css";
import FormComp from "./components/FormComp";
import Output from "./components/Output";
import { useState } from "react";

function App() {
  const defaultForm = {
    firstName: "",
    lastName: "",
    password: "",
    email: "",
  };
  const [formData, setFormData] = useState(defaultForm);
  const [submitData, setSubmitData] = useState(defaultForm);
  return (
    <div className="App">
      <FormComp
        formData={formData}
        setFormData={setFormData}
        defaultForm={defaultForm}
        submitData={submitData}
        setSubmitData={setSubmitData}
      />
      <Output
        submitData={submitData}
        setSubmitData={setSubmitData}
        defaultForm={defaultForm}
      />
    </div>
  );
}

export default App;
