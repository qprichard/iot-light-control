import React from 'react';
import Main from "./pages/main";
import Login from "./pages/login/container";
import AuthController from "./utils/AuthController";

import{ Switch, Route, Redirect, BrowserRouter as Router } from "react-router-dom";


function App() {
  return (
    <Router basename="/access-control">
      <div className="App">
        <AuthController>
          <Switch>
            <Route path="/home" component={ Main }/>
            <Route path="/login" component={ Login }/>
            <Redirect to="/home"/>
          </Switch>
        </AuthController>
      </div>
    </Router>
  );
}

export default App;
