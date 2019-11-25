export function getLocalStorage() {
  let ls = window.localStorage.getItem('userInfo') || '{}'
  if(ls) {
    ls = JSON.parse(ls)
  }


  return ls
}
