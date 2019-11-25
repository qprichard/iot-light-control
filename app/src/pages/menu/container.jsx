import React from "react";
import "../css/menu/menu.scss"

const Menu = ({ user }) => {

  if(!user) {
    return null;
  }
  
  return (
    <div className="menu">
      <div className="menu-title">
        IoT Access Control Management - {user.login}
      </div>
      <div className="menu-content">
      </div>
    </div>
  )
}

export default Menu;
