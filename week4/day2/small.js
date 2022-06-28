const container = document.getElementsByClassName("container");
const heading = document.getElementById("heading");
heading.innerText = "Toppings";
const burger = document.getElementById("burger");
burger.classList = "list-item";
const list = document.getElementById("list");
const li = document.createElement("li");
li.innerText = "Hot Dog";
list.append(li);
