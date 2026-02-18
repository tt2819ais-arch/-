import api from '@/services/api'

export default {
  loadPromoList () {
    return api().get('/promo')
  }
}



// WEBPACK FOOTER //
// src/services/promoHandler.js