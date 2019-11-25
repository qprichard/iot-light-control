import React from "react";
import "../css/menu/menu.scss"
import NavButton from "./navButton";

const Menu = ({ user, action }) => {
  if(!user) {
    return null;
  }

  return (
    <div className="menu">
      <div className="menu-title">
        IoT Access Control Management - {user.login}
      </div>
      <div className="menu-content">
        <NavButton name="General" action={ () => action('general') }/>
          <NavButton name="Users" action={ () => action("users") }/>
      </div>
    </div>
  )
}

export default Menu;
