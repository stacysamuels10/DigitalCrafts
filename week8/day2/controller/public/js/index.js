const sendData = async () => {
  const dataWeWant = await fetch("http://localhost:3030/ptes/get_pets", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  const json = await dataWeWant.json();
};

sendData();
