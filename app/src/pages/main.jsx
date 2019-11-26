import React from "react";
import "./css/main.scss";

import Menu from "./menu/container";
import Log from "./log/container";
import { getLocalStorage } from "../utils/utils"
import Management from "./management"

const Main = () => {
  const { user } = getLocalStorage()

  const [current, setCurrent] = React.useState('general')
  return (
    <div className="main">
      <div className="main-top">
        <Menu user={ user } action={ setCurrent }/>
      </div>
      <div className="main-container">
        <div className="main-management">
          <Management current={ current }/>
        </div>
        <div className="main-log">
          <Log/>
        </div>
      </div>
    </div>
  )
}

export default Main;
