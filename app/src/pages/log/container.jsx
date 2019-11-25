import React from "react";
import { fetch_logs } from "../../utils/api";
import "../css/log/log.scss";

const Log = () => {
  const [logs, setLogs] = React.useState({});


  const my_fetch = () => fetch_logs(10, setLogs)

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
          </tr>
        </thead>
        <tbody>
          {
            Object.entries(logs).map(([_, {id, card_uid, log_date}]) => (
              <tr>
                <td>{ id }</td>
                <td>{ card_uid }</td>
                <td>{log_date}</td>
              </tr>
            ))
          }
        </tbody>
      </table>
    </div>
  )
}

export default Log;
