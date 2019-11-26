import React from "react";
import { get_users, fetch_logs, create_user, delete_user } from "../../utils/api";


const Users = () => {

  const [users, setUsers] = React.useState({});
  const [authLogs, setAuthLogs] = React.useState({});

  const [form, setForm] = React.useState({});

  React.useEffect(() => {
    get_users(setUsers);
    fetch_logs(setAuthLogs, 10)
  }, []);

  const handleCreate = React.useCallback(() => { create_user(form, setUsers) }, [form]);
  const handleDelete = React.useCallback((card_uid) => {delete_user({card_uid}, setUsers)}, []);

  return(
    <div className="users-page">
      <div className="users-title">Users Management</div>
      <div className="user-list">
        <div className="user-list-title">
          User List
        </div>
        <table>
          <thead>
            <tr>
                <th>Login </th>
                <th>Card UID</th>
                <th>Last Name</th>
                <th>First Name</th>
                <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {
              Object.entries(users).map(([_, {id, last_name, first_name, login, card_uid}]) => (
                <tr key={id}>
                  <td>{ login }</td>
                  <td>{ card_uid }</td>
                  <td>{last_name}</td>
                  <td>{first_name}</td>
                  <td><button onClick={() => handleDelete(card_uid) }>delete</button></td>
                </tr>
              ))
            }
          </tbody>
        </table>
      </div>

      <div className="user-create">
        <div className="user-create-title">Add User</div>
        <form>
          <label>Login: </label>
          <input placeholder="login" maxLength= {8} onChange={({target}) =>setForm({...form, login: target.value})}/>

          <label>Password: </label>
          <input type="password" placeholder="password" onChange={({target}) =>setForm({...form, password: target.value})}/>

          <label>Last Name: </label>
          <input placeholder="last name" onChange={({target}) =>setForm({...form, last_name: target.value})}/>

          <label>First Name: </label>
          <input placeholder="first name" onChange={({target}) =>setForm({...form, first_name: target.value})}/>

            <label>card uid: </label>
            <select onChange={({target}) =>{setForm({...form, card_uid: target.value})} }>
              <option value=""></option>
              {
                Object.entries(authLogs).reduce((reducer, current) => {
                  if(!current || !current.length) {
                    return reducer;
                  }

                  const [_, { card_uid, granted}]  = current
                  if(!reducer.includes(card_uid) && !granted) {
                    reducer.push(card_uid)
                  }
                  return reducer;
                }, []).map((card_uid) =>(<option key={card_uid} value={card_uid}>{card_uid}</option>))
              }
            </select>
        </form>
        <button onClick={ handleCreate }>Create User</button>

      </div>
    </div>
  )
}

export default Users;
