<template>
  <div class="create-promo">
    <Header />
    <main>
      <div class="form-conteiner">
        <div class="form" style="width: 100%;">
          <div class="form-title">
            <section>
              <h2 class="text-center">Главная страница</h2>
            </section>
          </div>
          <form @submit.prevent="sendNewLogsFileData">
            <p style="color: #ccc; margin-top: 1%; margin-bottom: 1%; font-size: 13px;">Редактировать?</p>
            <input type="checkbox" v-model="checkBoxState" @click="onChange">
            <input type="submit" value="Изменить">
            <p style="color: #ccc; margin-top: 1%; margin-bottom: 1%; font-size: 13px;">Код страницы (Убедитесь что тут нет никаких ошибок):</p>
            <template v-if="readState == true">
              <prism-editor v-model="code" language="vue" :line-numbers="true" :readonly="readState" class="my-editor"/>
            </template>
            <template v-else>
              <textarea v-model="code" wrap="off" rows="400"/>
            </template>
          </form>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios'
import config from '@/config/config.js'
import iEH from '@/services/editFileHandler'
import Header from '@/components/includes/Header'
import PrismEditor from 'vue-prism-editor'

export default {
  data () {
    return {
      errorMessageStyle: 1,
      errorMessageType: null,
      errorMessage: null,
      /* Форма */
      checkBoxState: false,
      readState: true,
      code: null
    }
  },
  components: {
    Header,
    PrismEditor
  },
  mounted () {
    this.openLogsFile()
  },
  methods: {
    async sendNewLogsFileData () {
      if (this.code == null || !this.code === ' ') {
        this.errorMessageType = 1
        this.errorMessage = 'Поле для ввода кода пустое!'
        return
      }
      this.errorMessage = null

      const response = await axios({
        url: config.config.serverURL + '/edit/update',
        method: 'POST',
        data: {
          code: this.code
        }
      })

      if (response.data.fileChanged === true) {
        this.errorMessageType = 2
        setTimeout(() => {
          this.$router.push('/')
        }, 1500)
      } else {
        this.errorMessageType = 0
      }
      this.errorMessage = response.data.description
    },
    onChange () {
      this.readState = !this.readState
    },
    async openLogsFile () {
      const response = await iEH.loadFileDataToClient()
      if (response.data == null) {
        this.code = 'Ошибка при чтении файла!'
      } else {
        this.code = response.data
      }
    }
  }
}
</script>



// WEBPACK FOOTER //
// Edit.vue