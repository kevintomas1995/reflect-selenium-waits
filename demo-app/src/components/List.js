import React from "react";
import "./List.css";

function List(props) {
  return (
    <div className="list">
      <p className="list-header">{props.header}</p>
      {props.data.map((item) => {
        return (
          <li className="list-item" key={item.id}>
            {item.name}
          </li>
        );
      })}
    </div>
  );
}

export default List;
