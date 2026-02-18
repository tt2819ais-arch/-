<template>
  <div id="app">
    <!-- <Header /> -->
    <router-view/>
    <!-- <Footer /> -->
  </div>
</template>

<script>
import Header from '@/components/includes/Header'
import Footer from '@/components/includes/Footer'

export default {
  name: 'App',
  components: {
    Header,
    Footer
  }
}
</script>



// WEBPACK FOOTER //
// App.vue