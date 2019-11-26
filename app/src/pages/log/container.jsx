import React from "react";
import { fetch_logs } from "../../utils/api";
import "../css/log/log.scss";

const Log = () => {
  const [logs, setLogs] = React.useState({});


  const my_fetch = () => fetch_logs(setLogs,10)

  React.useEffect(() => {
    let inter = setInterval(my_fetch, 3000)

    return () => clearInterval(inter)
  }, []);



  return (
    <div className="log-container">
      <div className="log-title">Current Logs</div>
      <table>
        <thead>
          <tr>
              <th>ID </th>
              <th>Card UID</th>
              <th>Date</th>
              <th>Access</th>
          </tr>
        </thead>
        <tbody>
          {
            Object.entries(logs).map(([_, {id, card_uid, log_date, granted}]) => (
              <tr key={id}>
                <td>{ id }</td>
                <td>{ card_uid }</td>
                <td>{log_date}</td>
                <td>{ granted ? 'GRANTED' : 'REFUSED'}</td>
              </tr>
            ))
          }
        </tbody>
      </table>
    </div>
  )
}

export default Log;
