const container = document.getElementsByClassName("container");
const addTask = document.getElementById("addTask");
const toDoListDisplay = document.getElementById("appended-list");
const taskInput = document.getElementById("taskInput");

const printInput = () => {
  if (taskInput.value != "") {
    const task = document.createElement("li");
    const checkDone = document.createElement("button");
    checkDone.classList = "strikethrough";
    checkDone.innerText = "✓";
    const exDelete = document.createElement("button");
    exDelete.classList = "delete";
    exDelete.innerText = "X";
    task.innerText = taskInput.value;
    toDoListDisplay.append(task, checkDone, exDelete);
  }
};

const strikeDone = () => {
  console.log("hello");
};
//document.getElementById().style.property = new style;
addTask.onclick = printInput;
const checkDone = getElementsByClassName("strikethrough");
checkDone.onclick = strikeDone;
