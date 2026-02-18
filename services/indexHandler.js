import api from '@/services/api'

export default {
  getAllLogs () {
        return api().get('/', { withCredentials: true })
  }
}



// WEBPACK FOOTER //
// src/services/indexHandler.js