import React from "react";
import General from "./general/container";
import Users from "./users/container";

const getPage = (current) => {
  switch (current) {
    case "general":
      return <General/>
    case "users":
      return <Users/>
    default:
      return <General/>
  }
}

const Management = ({current}) => (
  <div className="management">
    { getPage(current) } 
  </div>
)

export default Management;
