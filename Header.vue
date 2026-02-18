<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="#">Логи | Barvikha 8</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <router-link class="nav-link" to="/">Главная</router-link>
      </li>
      <template v-if="logged == true">
        <li class="nav-item">
          <router-link class="nav-link" to="/promo">Промокоды</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/edit">Редактировать</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/dashboard">Мониторинг</router-link>
        </li>
      </template>
    </ul>
      <ul class="navbar-nav">
        <li class="nav-item">
          <template v-if="logged == true">
            <router-link class="nav-link" to="/log-out">Выйти</router-link>
          </template>
          <template v-else>
            <router-link class="nav-link" to="/login">Войти</router-link>
          </template>
        </li>
      </ul>
  </div>
</nav>
</template>

<script>
import LoginHandler from '@/services/LoginHandler.js'
export default {
  data () {
    return {
      logged: false
    }
  },
  mounted () {
    this.getLoginData()
  },
  methods: {
    async getLoginData () {
      try {
        const response = await LoginHandler.checkUserLoginSession()
        this.logged = response.data.logged
        if (this.logged === false && this.$route.name !== 'Login' && this.$route.name !== 'Reset-Password') {
          this.$router.push('/login')
        }
      } catch (ex) {
        console.log(this.$route.name)
        if (this.$route.name !== 'Error 404') {
          this.$router.push('/*')
        }
      }
    }
  }
}
</script>



// WEBPACK FOOTER //
// Header.vue