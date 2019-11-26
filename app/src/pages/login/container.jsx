import React from "react";
import "../css/login/login.scss";
import { fetch_login } from "../../utils/api"
import { useHistory } from "react-router-dom";

const Login = () => {

  const history = useHistory();

  const [form, setForm] = React.useState({});
  const [token, setToken] = React.useState(null);

  const handleLogin = React.useCallback(() => {
    const {login, password} = form;

    if(login && login.length && password && password.length) {
      fetch_login(form, setToken)
    }
  }, [form])

  React.useEffect(() => {
    if(token) {
      history.push('/home')
    }
  }, [token, history]);

  return (
    <div className="login-container">
      <h1>Login to your Account</h1>
      <form>
        <label>Login</label>
        <input onChange={({target}) => setForm({...form, login: target.value})} placeholder="login"/>

        <label>Password</label>
        <input type="password" onChange={({target}) => setForm({...form, password: target.value})} placeholder="password"/>
      </form>

      <button onClick={ handleLogin }>login</button>
    </div>
  );
}

export default Login;
