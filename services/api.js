import axios from 'axios'
import config from '../config/config'

export default () => {
  return axios.create({
    baseURL: config.config.serverURL
  })
}



// WEBPACK FOOTER //
// src/services/api.js