import logo from "./logo.svg";
import "./App.css";
import Student from "./Student";

function App() {
  const name = "Stacy!";
  const students = ["Joe", "Violet", "Olivia", "Blke"];
  return (
    <div className="App">
      <h1>Hello {name}</h1>
      {students.map((student) => (
        <>
          <Student student={student} />
        </>
      ))}
      <Student student={"Stacy"} />
    </div>
  );
}

export default App;
