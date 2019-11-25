import { API_URL } from "../config";


export async function fetch_api(method, url, data) {
  const options = {
    'method': method,
    'mode': "cors",
    'headers': {
      "Content-type": "application/json",
    },
  }
  if (["PATCH", "POST", "PUT", "DELETE"].includes(method)) {
    options['body'] = data ? JSON.stringify(data) : {};
  }

  let localStorage = window.localStorage.getItem('userInfo')
  if (localStorage) {
    localStorage = JSON.parse(localStorage)

    if(localStorage.token) {
      options.headers['Authorization'] = localStorage.token
    }
  }

  const response =  await fetch(`${API_URL}${url}`, options)

  if(response.status === 401) {
    window.localStorage.removeItem('userInfo')
  }

  return response
}


export function fetch_login(data, set) {
  fetch_api('POST', '/authenticate', data).then(
    (response) => {
      if(response.status !== 200) {
        return;
      }
      response.json().then(
        (rep) => {
          window.localStorage.setItem('userInfo', JSON.stringify(rep))
          set(rep)
        }
      ).catch(() => { return;  })
    }
  ).catch((e) => { return; })
}

export function fetch_logs(limit, set) {
  fetch_api('GET', `/auth_log?limit=${limit}`).then(
    async (response) => {
      if(response.status !== 200) {
        return;
      }
      const rep = await response.json()
      set(rep)
    }
  ).catch((e) => { return; })
}
