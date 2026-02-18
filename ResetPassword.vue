<template>
  <div class="index">
    <Header />
    <main>
      <div class="form-conteiner">
        <div class="form">
          <div class="form-title">
              <section>
                  <h2 class="text-center">Восстановление пароля</h2>
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
          <form @submit.prevent="sendResetLoginData">
            <p style="color: #ccc; margin-top: 1%; margin-bottom: 1%; font-size: 13px;">Имя пользователя:</p>
            <input v-model="login" type="text" :disabled="resetPasswordStep != 0">

            <template v-if="resetPasswordStep > 0">
              <p style="color: #ccc; margin-top: 1%; margin-bottom: 1%; font-size: 13px;">Код в сообщении:</p>
              <input v-model="key" type="password" :disabled="resetPasswordStep != 1">
            </template>
            <template v-if="resetPasswordStep == 2">
              <p style="color: #ccc; margin-top: 1%; margin-bottom: 1%; font-size: 13px;">Новый пароль:</p>
              <input v-model="password" type="password">
            </template>
            <input type="submit" :value="`${buttonText}`">
          </form>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios'
import crypto from 'crypto'
import config from '@/config/config.js'

import LoginHandler from '@/services/LoginHandler.js'
import Header from '@/components/includes/Header'

export default {
  data () {
    return {
      errorMessageStyle: 1,
      errorMessageType: null,
      resetPasswordStep: 0,
      errorMessage: null,
      // форма
      login: null,
      key: null,
      password: null,
      //
      serverSideKey: null,
      buttonText: 'Продолжить'
    }
  },
  mounted () {
    this.getLoginData()
  },
  components: {
    Header
  },
  methods: {
    generateErrorMessage (type, message) {
      this.errorMessageType = type
      this.errorMessage = message
    },
    async getLoginData () {
      try {
        const response = await LoginHandler.checkUserLoginSession()
        if (response.data.logged === true) {
          this.$router.push('/')
        }
      } catch (ex) {
        console.log(ex)
      }
    },
    async sendResetLoginData () {
      switch (this.resetPasswordStep) {
        case 0: {
          if (this.login == null || this.login === '') {
            this.generateErrorMessage(1, 'Поле для ввода логина не заполнено!')
            return
          }
          const response = await axios({
            url: config.config.serverURL + '/reset-password',
            method: 'POST',
            data: {
              Login: this.login,
              Type: 1
            }
          })

          this.generateErrorMessage(response.data.error, response.data.description)

          if (response.data.error === 2) {
            this.resetPasswordStep = 1
            this.serverSideKey = response.data.secretKey
          }
          break
        }
        case 1: {
          if (this.key == null || this.key === '') {
            this.generateErrorMessage(1, 'Поле для ввода ключа не заполнено!')
            return
          }
          if (parseInt(this.key, 10) !== this.serverSideKey) {
            this.generateErrorMessage(0, 'Ваш секретный ключ не совпадает с ведённым!')
            return
          }
          this.resetPasswordStep = 2
          this.buttonText = 'Сбросить'
          break
        }
        case 2: {
          if (this.password == null || this.password === '') {
            this.generateErrorMessage(1, 'Поле для ввода пароля не заполнено!')
            return
          }
          if (this.password.length < 6 || this.password.length > 24) {
            this.generateErrorMessage(1, 'Длина пароля от 6-ти до 24-ёх символов!')
            return
          }
          const response = await axios({
            url: config.config.serverURL + '/reset-password',
            method: 'POST',
            data: {
              Login: this.login,
              password: crypto.createHash('md5').update(this.password).digest('hex'),
              Type: 2
            }
          })
          this.generateErrorMessage(response.data.error, response.data.description)

          if (response.data.error === 2) {
            setTimeout(() => {
              this.$router.push('/')
            }, 1500)
          }
          break
        }
      }
    }
  }
}
</script>



// WEBPACK FOOTER //
// ResetPassword.vue