const submit = document.getElementById("submit");

const sendData = async () => {
  const name = document.getElementById("name").value;
  const address = document.getElementById("address").value;
  const reviewScore = document.getElementById("reviewScore").value;
  const data = {
    name: name,
    address: address,
    reviewScore: reviewScore,
    createdAt: new Date(),
    updatedAt: new Date(),
  };
  const dataWeAreSending = await fetch(
    "http://localhost:3030/restaurants/create_restaurant",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    }
  );
  console.log("data", data);
  console.log(dataWeAreSending);
  const json = await dataWeAreSending.json();
  console.log(json);
};

submit.onclick = () => sendData();
