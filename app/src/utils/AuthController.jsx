import React from "react";
import { useHistory, useLocation } from "react-router-dom";

const AuthController = ({ children }) => {
  const location = useLocation()
  const history = useHistory()
  let localStorage = window.localStorage.getItem('userInfo')
  localStorage = JSON.parse(localStorage)

  React.useEffect(() => {
    if(localStorage && localStorage.user) {
      window.user = localStorage.user
    }

    if(location.pathname !== "/login" && (!localStorage || !localStorage.token)) {
      history.push('/login')
    }
  }, [location, history, localStorage])

  return children
}

export default AuthController;
