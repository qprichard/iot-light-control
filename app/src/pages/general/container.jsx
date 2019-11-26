import React from "react";
import { fetch_stats } from "../../utils/api";
import {
  BarChart as Bc, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
  LineChart, Line,
} from 'recharts';


const MyLineChart = ({data, color}) => {
  if(!data || !data['logs']) {
    return null;
  }

  const loginList = []
  const my_data = Object.entries(data.logs).map(([date, user]) => {
    const logins = Object.entries(user).reduce((reducer, [_,{count, login}]) => {
      reducer[login] = count
      if(!loginList.includes(login)) {
        loginList.push(login)
      }
      return reducer;
    }, {})
    return {
      date,
      ...logins
    }
  })

  return (
    <LineChart
       width={1000}
       height={300}
       data={my_data}
       margin={{
         top: 5, right: 30, left: 20, bottom: 5,
       }}
     >
       <CartesianGrid strokeDasharray="3 3" />
       <XAxis dataKey="date" />
       <YAxis />
       <Tooltip />
       <Legend />
       {
         loginList.map((login) => {
           return (
             <Line dataKey={login} stroke={`#${color}`} />
           )
         })
       }
     </LineChart>
  )
}






const BarChart = ({data}) => {
  if(!data || !data['date_count']) {
    return null
  }
  const my_data = Object.entries(data['date_count']).map(([key, {granted, refused}]) => ({name: key, granted, refused}))
  return (
    <Bc
        width={1000}
        height={300}
        data={my_data}
        margin={{
          top: 5, right: 30, left: 20, bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="granted" fill="#24db68" />
        <Bar dataKey="refused" fill="#93000d" />
      </Bc>
  )
}
const General = () => {

  const [data, setLogs] = React.useState({});
  const [filter, setFilter] = React.useState('hour')

  const color = React.useMemo(() => Math.floor(Math.random()*16777215).toString(16), [])
  console.log(filter)

  const my_fetch = () => fetch_stats(setLogs,filter)

  React.useEffect(() => {
    let inter = setInterval(my_fetch, 3000)

    return () => clearInterval(inter)
  }, [my_fetch]);

  return(
    <div className="general-page">
      <div className="general-page-title"> General Statistics</div>
      <div className="general-charts">
        <div className="charts-management">
          <form>
            <label>day</label>
            <input type="radio" name="type" value="day" onClick={({target}) => setFilter(target.value)}/>
            <label>hour</label>
            <input type="radio" name="type" value="hour" onClick={({target}) => setFilter(target.value)}/>
            <label>minute</label>
            <input type="radio" name="type" value="minute"onClick={({target}) => setFilter(target.value)}/>
          </form>
        </div>
        <div className="charts-display">
          <BarChart data={data}/>
          <MyLineChart data={data} color={color}/>
        </div>

      </div>
    </div>
  )
}

export default General;
