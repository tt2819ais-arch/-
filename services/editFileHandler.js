import api from '@/services/api'

export default {
  loadFileDataToClient () {
    return api().get('/edit')
  }
}



// WEBPACK FOOTER //
// src/services/editFileHandler.js