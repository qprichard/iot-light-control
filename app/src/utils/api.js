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

export function fetch_logs(set, limit) {
  const url = limit ? `/auth_log?limit=${limit}` : "/auth_log"
  fetch_api('GET', url).then(
    async (response) => {
      if(response.status !== 200) {
        return;
      }
      const rep = await response.json()
      set(rep)
    }
  ).catch((e) => { return; })
}

export function get_users(set) {
  fetch_api('GET', '/users').then(
    async(response) => {
      if(response.status !== 200) {
        return;
      }
      const rep = await response.json()
      set(rep)
    }
  ).catch(() => {return; })
}

export function create_user(data, set) {
  fetch_api('POST', '/users', data).then(
    async(response) => {
      if(response.status !== 200) {
        return;
      }
      const rep = await response.json()
      set(rep)
    }
  ).catch(() => {return; })
}

export function delete_user(data, set) {
  fetch_api('DELETE', '/users', data).then(
    async(response) => {
      if(response.status !== 200) {
        return;
      }
      const rep = await response.json()
      set(rep)
    }
  ).catch(() => {return; })
}

export function fetch_stats(set, filter) {
  const url = filter ? `/stats?filter=${filter}` : '/stats'
  fetch_api('GET', url).then(
    async(response) => {
      if(response.status !== 200) {
        return;
      }
      const rep = await response.json()
      set(rep)
    }
  ).catch(() => {return; })
}
