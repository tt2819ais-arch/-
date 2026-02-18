<template>
  <div class="create-promo">
    <Header />
    <main>
      <div class="form-conteiner">
        <div class="form">
          <div class="form-title">
              <section>
                  <h2 class="text-center">Создание промокода</h2>
              </section>
          </div>
          <template v-if="errorMessageStyle == false">
            <template v-if="errorMessage != null">
              <template v-if="errorMessageType == 0">
                <div class="form-errors">
                  <ul>
                    <li>{{ errorMessage }}</li>
                  </ul>
                </div>
              </template>
              <template v-else-if="errorMessageType == 1">
                <div class="form-warning">
                  <ul>
                    <li>{{ errorMessage }}</li>
                  </ul>
                </div>
              </template>
              <template v-else-if="errorMessageType == 2">
                <div class="form-success">
                  <ul>
                    <li>{{ errorMessage }}</li>
                  </ul>
                </div>
              </template>
            </template>
          </template>
          <template v-else-if="errorMessageStyle == true">
            <template v-if="errorMessage != null">
              <template v-if="errorMessageType == 0">
                <div class="alert alert-danger">
                  <strong>Ошибка!</strong> {{ errorMessage }}
                </div>
              </template>
              <template v-else-if="errorMessageType == 1">
                <div class="alert alert-warning">
                  <strong>Внимание!</strong> {{ errorMessage }}
                </div>
              </template>
              <template v-else-if="errorMessageType == 2">
                <div class="alert alert-success">
                  <strong>Успешно!</strong> {{ errorMessage }}
                </div>
              </template>
            </template>
          </template>
          <form @submit.prevent="sendCreatePromoData">
            <p style="color: #ccc; margin-top: 1%; margin-bottom: 1%; font-size: 13px;">Название промокода:</p>
            <input v-model="promo" type="text">

            <p style="color: #ccc; margin-top: 1%; margin-bottom: 1%; font-size: 13px;">Ссылка на канал/группу и тд (можно оставить пустым):</p>
            <input v-model="link" type="text">

            <p style="color: #ccc; margin-top: 1%; margin-bottom: 1%; font-size: 13px;">Для какого сервера:</p>
            <select v-model="serverType" @change="onChange()" style="background: #413F43; color: #ccc;">
              <option value=null>Не выбран</option>
              <option value=0>SanTrope</option>
              <option value=1>Barvikha</option>
            </select>

            <template v-if="serverType == 0">
              <p style="color: #ccc; margin-top: 1%; margin-bottom: 1%; font-size: 13px;">Номер сервера:</p>
              <select v-model="serverNumber" style="background: #413F43; color: #ccc;">
                <option value="null">Не выбран</option>
                <option value="1">Сервер #1</option>
                <option value="2">Сервер #2</option>
                <option value="3">Сервер #3</option>
                <option value="4">Сервер #4</option>
                <option value="5">Сервер #5</option>
                <option value="6">Сервер #6</option>
              </select>
            </template>
            <template v-else-if="serverType == 1">
              <p style="color: #ccc; margin-top: 1%; margin-bottom: 1%; font-size: 13px;">Номер сервера:</p>
              <select v-model="serverNumber" style="background: #413F43; color: #ccc;">
                <option value="null">Не выбран</option>
                <option value="1">Сервер #1</option>
                <option value="2">Сервер #2</option>
                <option value="3">Сервер #3</option>
                <option value="4">Сервер #4</option>
              </select>
            </template>
            <input type="submit" value="Создать">
          </form>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios'
import config from '@/config/config.js'
import Header from '@/components/includes/Header'

export default {
  data () {
    return {
      errorMessageStyle: 1,
      errorMessageType: null,
      errorMessage: null,
      /* Форма */
      promo: null,
      link: null,
      serverType: null,
      serverNumber: null
    }
  },
  components: {
    Header
  },
  methods: {
    async sendCreatePromoData () {
      var regex = new RegExp('^[0-9a-zA-Z]{1,30}$')

      if (this.promo == null || !this.promo.match(regex)) {
        this.errorMessageType = 1
        this.errorMessage = 'Промокод имеет не правильный формат!'
        return
      }
      if (this.serverType == null) {
        this.errorMessageType = 1
        this.errorMessage = 'Вы не выбрали для какого сервера промокод!'
        return
      }
      if (this.serverNumber == null) {
        this.errorMessageType = 1
        this.errorMessage = 'Вы не выбрали номер сервера!'
        return
      }
      this.errorMessage = null

      const response = await axios({
        url: config.config.serverURL + '/promo/create',
        method: 'POST',
        data: {
          promo: this.promo,
          link: this.link,
          serverType: this.serverType,
          serverNumber: this.serverNumber
        }
      })

      if (response.data.promoCreated === true) {
        this.errorMessageType = 2
        setTimeout(() => {
          this.$router.push('/promo')
        }, 1500)
      } else {
        this.errorMessageType = 0
      }
      this.errorMessage = response.data.description
    },
    onChange () {
      this.serverNumber = null
    }
  }
}
</script>



// WEBPACK FOOTER //
// createPromo.vue