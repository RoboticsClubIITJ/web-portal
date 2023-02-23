import axios from 'axios'

const instance = axios.create({
  baseURL: 'localhost:8000/api',
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken'
})

instance.interceptors.request.use(config => {
  config.headers.post['Content-Type'] = 'multipart/form-data'
  return config
})

export { instance }
