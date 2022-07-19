console.log("i'm on the client");

const button = document.getElementById("button");

const sendData = async () => {
  const input = document.getElementById("input").value;
  const data = {
    message: input,
  };
  const dataWeAreSending = await fetch("http://localhost:3030/home", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  const json = await dataWeAreSending.json();
};

button.onclick = () => sendData();
