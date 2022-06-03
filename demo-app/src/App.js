import "./App.css";
import List from "./components/List";
import { data } from "./data";
import { useState, useEffect } from "react";

function App() {
  const [renderTimeOut, setRenderTimeOut] = useState(false);
  const [fakeData, setFakeData] = useState(undefined);

  useEffect(() => {
    setTimeout(() => {
      setRenderTimeOut(true);
    }, 3000);
  }, []);

  // get data from the fake api endpoint
  useEffect(() => {
    const getData = async () => {
      const apiResponse = await fetch(
        "https://my-json-server.typicode.com/kevintomas1995/logRocket_searchBar/languages"
      );
      const data = await apiResponse.json();
      setFakeData(data);
    };
    getData();
  }, []);

  return (
    <div className="app">
      <div className="app-header">Simple React Demo App</div>
      <div className="app-body">
        <div className="instant">
          <List data={data} header="Instantly:" />
        </div>

        {fakeData && (
          <div className="miliseconds">
            <List data={fakeData} header="Miliseconds:" />
          </div>
        )}

        {renderTimeOut && (
          <div className="timeout">
            <List data={data} header="3 seconds:" />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
