import React from "react";
import "./css/main.scss";

import Menu from "./menu/container";
import Log from "./log/container";
import { getLocalStorage } from "../utils/utils"

const Main = () => {
  const { user } = getLocalStorage()
  return (
    <div className="main">
      <div className="main-top">
        <Menu user={ user }/>
      </div>
      <div className="main-container">
        <div className="main-management">
          Here, there will be the management view
        </div>
        <div className="main-log">
          <Log/>
        </div>
      </div>
    </div>
  )
}

export default Main;
