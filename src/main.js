// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import VueCookies from 'vue-cookies'
import { routes } from './router/index'
import 'prismjs'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import './static/main.css'
import 'prismjs/themes/prism-tomorrow.css'
import 'vue-prism-editor/dist/VuePrismEditor.css'

Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(VueCookies)

const router = new VueRouter({
  mode: 'history',
  routes
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})



// WEBPACK FOOTER //
// src/main.js