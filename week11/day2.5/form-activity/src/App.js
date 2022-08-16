import "./App.css";
import FormComp from "./components/FormComp";
import Output from "./components/Output";
import { useState } from "react";

function App() {
  const defaultForm = {
    name: "",
    password: "",
    address: "",
    email: "",
  };
  const [formData, setFormData] = useState(defaultForm);
  return (
    <div className="App">
      <FormComp
        formData={formData}
        setFormData={setFormData}
        defaultForm={defaultForm}
      />
      <Output
        formData={formData}
        setFormData={setFormData}
        defaultForm={defaultForm}
      />
    </div>
  );
}

export default App;
