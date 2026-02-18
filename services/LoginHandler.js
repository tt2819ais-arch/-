import api from '@/services/api'

export default {
  checkUserLoginSession () {
    return api().get('/login', {withCredentials: true})
  }
}



// WEBPACK FOOTER //
// src/services/LoginHandler.js