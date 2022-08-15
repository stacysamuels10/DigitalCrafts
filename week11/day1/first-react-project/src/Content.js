import React from "react";

import { useState } from "react";
export default function Content() {
  const [listItem, setListItem] = useState("");
  const [toDoList, setToDoList] = useState([]);
  const addToList = (event) => {
    event.preventDefault();
    setToDoList([...toDoList, listItem]);
    setListItem("");
  };
  const deleteTodo = (item) => {
    const filtereditemList = toDoList.filter((listItem) => item !== listItem);
    setToDoList(filtereditemList);
  };
  return (
    <div className="Content">
      <h1>To Do List</h1>
      <form onSubmit={addToList}>
        <label>
          Enter your to do list item:
          <input
            type="text"
            value={listItem}
            onChange={(e) => setListItem(e.target.value)}
          />
        </label>
        <input type="submit" />
      </form>
      <ul>
        {toDoList.map((listItem) => (
          <>
            <li>{listItem}</li>
            <button onClick={() => deleteTodo(listItem)}>X</button>
          </>
        ))}
      </ul>
    </div>
    //const items = [] on submit append to array, then map items in list
  );
}
