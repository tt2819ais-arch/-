<template>
  <div class="index">
    <Header />
  </div>
</template>

<script>
import LoginHandler from '@/services/LoginHandler.js'
import Header from '@/components/includes/Header'

export default {
  mounted () {
    this.getLoginData()
  },
  components: {
    Header
  },
  methods: {
    async getLoginData () {
      const response = await LoginHandler.checkUserLoginSession()
      if (response.data.logged === false) {
        this.$router.push('/login')
      } else {
        this.$cookies.remove('username')
        this.$cookies.remove('password')
        this.$router.push('/login')
      }
    }
  }
}
</script>



// WEBPACK FOOTER //
// Logout.vue