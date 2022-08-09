export default function Student(props) {
  return (
    <>
      <h2 key={props.student}>{props.student}</h2>
      <button onClick={() => console.log(props.student)}>Click me</button>
    </>
  );
}
