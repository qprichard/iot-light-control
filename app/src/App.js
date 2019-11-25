import React from 'react';
import Main from "./pages/main";
import Login from "./pages/login/container";
import AuthController from "./utils/AuthController";

import{ Switch, Route, BrowserRouter as Router } from "react-router-dom";


function App() {
  React.useEffect(() => {
    window.localStorage.removeItem('userInfo')
  }, [])
    return (
    <Router basename="/access-control">
      <div className="App">
        <AuthController>
          <Switch>
            <Route path="/home" component={ Main }/>
            <Route path="/login" component={ Login }/>
          </Switch>
        </AuthController>
      </div>
    </Router>
  );
}

export default App;
