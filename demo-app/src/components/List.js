import React, { useState } from "react";
import "./List.css";

function List(props) {
  const [isClicked, setIsCLicked] = useState(false);
  const clickHandler = () => {
    setIsCLicked(!isClicked);
  };

  return (
    <div className="list" onClick={clickHandler}>
      <p className="list-header">{props.header}</p>
      {props.data.map((item) => {
        return (
          <li
            key={item.id}
            style={isClicked ? { color: "white" } : { color: "black" }}
            className="list-item"
          >
            {item.name}
          </li>
        );
      })}
    </div>
  );
}

export default List;
