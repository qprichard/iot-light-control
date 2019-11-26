import React from "react";

const NavButton = ({ name, action }) => {
  const buttonAction = React.useCallback(() => action(), [action]);

  return(
    <div onClick = { buttonAction } className="nav-button">
      { name }
    </div>
  )
}

export default NavButton;
