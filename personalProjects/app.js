const logFormData = (e) => {
  e.preventDefault();
  const formToSend = {};
  for (const input of e.target.children) {
    formToSend[input.name] = input.value;
  }
};

const form = document.getElementById("form");

form.onsubmit = (e) => logFormData(e);
