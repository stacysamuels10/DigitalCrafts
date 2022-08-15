import "./App.css";
import { useState } from "react";
import { students, tas } from "./dummydata";
import Header from "./Header";
import Footer from "./Footer";
import AdBar from "./AdBar";
import MenuBar from "./MenuBar";
import Content from "./Content";

//hook
// to change state in functional components
function App() {
  // this is the syntax to create a useState hook
  // const [stateVariable, functionToChangeTheStateVariable] = useState()
  const [counter, setCounter] = useState(0);
  const [mood, setMood] = useState("😄");
  return (
    <div className="App">
      <Header />
      <MenuBar />
      <Content />
      <AdBar />
      <Footer />
      {/* <h1>Counter {counter}</h1>
      <button onClick={() => setCounter(() => counter + 1)}>+</button>
      <button onClick={() => setCounter(() => counter - 1)}>-</button>
      <h1>How are you feeling today?</h1>
      <h1>{mood ? "😄" : "🙁"}</h1>
      <button onClick={() => setMood(!mood)}>Change Mood</button> */}
    </div>
  );
}

export default App;
