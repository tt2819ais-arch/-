<template>
  <div class="index">
    <Header />
    <main>
      <div class="form-conteiner">
        <div class="form">
          <div class="form-title">
              <section>
                  <h2 class="text-center">Авторизация</h2>
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
          <form @submit.prevent="sendLoginData">
            <p style="color: #ccc; margin-top: 1%; margin-bottom: 1%; font-size: 13px;">Имя пользователя:</p>
            <input v-model="username" type="text">

            <p style="color: #ccc; margin-top: 1%; margin-bottom: 1%; font-size: 13px;">Пароль:</p>
            <input v-model="password" type="password">

            <input type="submit" value="Авторизоваться">
            <div class="text-center">
              <router-link to="reset-password" class="reset-message">Забыли пароль? Восстановите его!</router-link>
            </div>
          </form>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import LoginHandler from '@/services/LoginHandler.js'
import axios from 'axios'
import crypto from 'crypto'
import config from '@/config/config.js'
import Header from '@/components/includes/Header'

export default {
  data () {
    return {
      errorMessageStyle: 1,
      errorMessageType: null,
      logged: false,
      errorMessage: null,
      username: null,
      password: null
    }
  },
  components: {
    Header
  },
  mounted () {
    this.getLoginData()
  },
  methods: {
    async getLoginData () {
      try {
        const response = await LoginHandler.checkUserLoginSession()
        if (response.data.logged === true) {
          this.$router.push('/')
        } else {
          this.errorMessageType = 1
          this.errorMessage = response.data.description
        }
      } catch (ex) {
        console.log(ex)
      }
    },
    async sendLoginData () {
      if (this.username == null || this.username === '') {
        this.errorMessageType = 1
        this.errorMessage = 'Поле для ввода логина не заполнено!'
        return
      }
      if (this.password == null || this.password === '') {
        this.errorMessageType = 1
        this.errorMessage = 'Поле для ввода пароля не заполнено!'
        return
      }
      this.errorMessage = null
      this.password = crypto.createHash('md5').update(this.password).digest('hex')
      const response = await axios({
        url: config.config.serverURL + '/login',
        method: 'POST',
        data: {
          username: this.username,
          password: this.password
        }
      })

      this.logged = response.data.logged
      if (this.logged === true) {
        this.errorMessageType = 2
        this.$cookies.set('username', this.username, new Date(Date.now() + 86400 * 5 * 1000), null, null, false)
        this.$cookies.set('password', this.password, new Date(Date.now() + 86400 * 5 * 1000), null, null, false)
        setTimeout(() => {
          this.$router.push('/')
        }, 1500)
      } else {
        this.errorMessageType = 0
      }
      this.errorMessage = response.data.description
    }
  }
}
</script>



// WEBPACK FOOTER //
// Login.vue