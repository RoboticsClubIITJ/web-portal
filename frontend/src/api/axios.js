import axios from 'axios'

const instance = axios.create({
  baseURL: 'http://localhost:8080/api',
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken'
})

instance.interceptors.request.use(config => {
  config.headers.post['Content-Type'] = 'multipart/form-data'
  return config
})

export { instance }
