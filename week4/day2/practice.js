console.log(document);

//document.
//getElementById
const button1 = parseInt(document.getElementById("button1").innerText);
const button2 = parseInt(document.getElementById("button2").innerText);

const addition = document.getElementById("addition");

const buttons = document.getElementsByTagName("button");
for (const button of buttons) {
  console.log(button.innerText);
}
