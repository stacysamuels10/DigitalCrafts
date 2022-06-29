let count = 0;
const container = document.getElementsByClassName("container");
const addTask = document.getElementById("addTask");
const toDoListDisplay = document.getElementById("appended-list");
const taskInput = document.getElementById("taskInput");

const printInput = () => {
  if (taskInput.value != "") {
    const task = document.createElement("li");
    task.classList = `taskAdded${count}`;
    const checkDone = document.createElement("button");
    checkDone.classList = `strikethrough${count}`;
    const exDelete = document.createElement("button");
    checkDone.innerText = "✓";
    exDelete.classList = `delete${count}`;
    exDelete.innerText = "X";
    task.innerText = taskInput.value;
    toDoListDisplay.append(task, checkDone, exDelete);
    exDelete.onclick = strikeDone;
    checkDone.onclick = strikeDone;
  }
  count++;
};

const strikeDone = () => {
  let trying = document.getElementsByClassName("task").value;
  console.log(trying);
  //figure out count from classList
  //apply count to task
  //new variable =
};
//document.getElementById().style.property = new style;
addTask.onclick = printInput;
