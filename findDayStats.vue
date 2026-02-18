<template>
  <div class="create-promo">
    <Header />
    <main>
      <div class="form-conteiner">
        <div class="form">
          <div class="form-title">
              <section>
                  <h2 class="text-center">Поиск статистики за день</h2>
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
          <form @submit.prevent="sendFDData">
            <p style="color: #ccc; margin-top: 1%; margin-bottom: 1%; font-size: 13px;">Дата:</p>
            <input v-model="date" type="date">

            <input type="submit" value="Найти">
          </form>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import Header from '@/components/includes/Header'

export default {
  data () {
    return {
      errorMessageStyle: 1,
      errorMessageType: null,
      errorMessage: null,
      /* Форма */
      date: null
    }
  },
  components: {
    Header
  },
  methods: {
    async sendFDData () {
      if (this.date === null || this.date === '') {
        this.errorMessageType = 1
        this.errorMessage = 'Вы не выбрали желаемую дату!'
        return
      }
      this.errorMessage = null

      this.$router.push({
        path: '/API',
        query: {
          method: 'findDayStats',
          date: this.date
        }
      })
    }
  }
}
</script>



// WEBPACK FOOTER //
// findDayStats.vue