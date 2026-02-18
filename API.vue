<template>
  <div class="api">
    <Header />
    <!-- IP Info -->
    <template v-if="APIPage == 1">
      <div class="logs">
        <p style="color: #ccc; font-size: 15px; font-weight: bold;">Ссылка для ютубера: <a>http://{{ serverTypeLink[this.params.serverType] }}/application/controllers/cpromo.php?yt={{ this.params.promocode }}&sT={{ this.params.serverType }}&s={{ this.params.server }}</a></p>
        <p style="color: #ccc; font-size: 15px; font-weight: bold;">Сервер: {{ serverTypeName[this.params.serverType] }}.<br>Номер сервера: {{ this.params.server }}</p>
        <br>
        <div class="table-container">
          <table>
            <tr>
              <th>Дата</th>
              <th>Переходов</th>
              <th>Скачиваний</th>
              <th>Зарегистрировано</th>
              <th>Отыграно часов</th>
            </tr>
            <tr>
              <td>Всего:</td>
              <td>{{ totalPromotions.totalTransitions }}</td>
              <td>{{ totalPromotions.totalDownloads }}</td>
              <td>{{ totalPromotions.totalRegistered }}</td>
              <td>{{ totalPromotions.totalPlayed }}</td>
            </tr>
            <tr>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
            </tr>
            <tr v-for="promo in promoStats" :key="promo.ID">
              <td>{{ promo.date }}</td>
              <td>{{ promo.transitions }}</td>
              <td>{{ promo.downloads }}</td>
              <td>{{ promo.registered }}</td>
              <td>{{ Math.round(promo.hoursPlayed / 60) }}</td>
            </tr>
          </table>
        </div>
      </div>
    </template>
    <!-- Статистика промокода -->
    <template v-else-if="APIPage == 2">
      <div class="logs">
        <template v-if="promoStats != null && promoStats.length > 0">
          <p style="color: #ccc; font-size: 15px; font-weight: bold;">Реферальная ссылка: <a>http://{{ serverTypeLink[this.params.serverType] }}/application/controllers/cpromo.php?yt={{ this.params.promoCode }}&sT={{ this.params.serverType }}&s={{ this.params.server }}</a></p>
          <p style="color: #ccc; font-size: 15px; font-weight: bold;">Сервер: {{ serverTypeName[this.params.serverType] }}.<br>Номер сервера: {{ this.params.server }}</p>
          <br>
          <div class="table-container">
            <table>
              <tr>
                <th>Дата</th>
                <th>Переходов</th>
                <th>Скачиваний</th>
                <th>Зарегистрировано</th>
                <th>Отыграно часов</th>
              </tr>
              <tr>
                <td>Всего:</td>
                <td>{{ totalPromotions.totalTransitions }}</td>
                <td>{{ totalPromotions.totalDownloads }}</td>
                <td>{{ totalPromotions.totalRegistered }}</td>
                <td>{{ totalPromotions.totalPlayed }}</td>
              </tr>
              <tr>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
              </tr>
              <tr v-for="promo in promoStats" :key="promo.ID">
                <td>{{ promo.date }}</td>
                <td>{{ promo.transitions }}</td>
                <td>{{ promo.downloads }}</td>
                <td>{{ promo.registered }}</td>
                <td>{{ Math.round(promo.hoursPlayed / 60) }}</td>
              </tr>
            </table>
          </div>
        </template>
        <template v-else>
          <section>
            <h3>Для данного промокода пока нет статистики!</h3>
          </section>
        </template>
      </div>
    </template>
    <!-- Статистика промокода -->
    <template v-else-if="APIPage == 3">
      <div class="logs">
        <template v-if="promoStats != null && promoStats.length > 0">
          <p style="color: #ccc; font-size: 15px; font-weight: bold;">Статистика всех промокодов, со всех проектов и серверов за один день.<br>Дата: <a>{{ this.params.date }}</a></p>
          <br>
          <div class="table-container">
            <table>
              <tr>
                <th>Проект(сервер)</th>
                <th>Промокод</th>
                <th>Переходов</th>
                <th>Скачиваний</th>
                <th>Зарегистрировано</th>
                <th>Отыграно часов</th>
              </tr>
              <tr>
                <td>Всего:</td>
                <td>-</td>
                <td>{{ totalPromotions.totalTransitions }}</td>
                <td>{{ totalPromotions.totalDownloads }}</td>
                <td>{{ totalPromotions.totalRegistered }}</td>
                <td>{{ totalPromotions.totalPlayed }}</td>
              </tr>
              <tr>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
              </tr>
              <tr v-for="promo in promoStats" :key="promo.ID">
                <td>{{ serverTypeName[promo.serverType] }}({{ promo.server }})</td>
                <td>{{ promo.promoname }}</td>
                <td>{{ promo.transitions }}</td>
                <td>{{ promo.downloads }}</td>
                <td>{{ promo.registered }}</td>
                <td>{{ Math.round(promo.hoursPlayed / 60) }}</td>
              </tr>
            </table>
          </div>
        </template>
        <template v-else>
          <section>
            <h3>Для данной даты пока нет статистики!</h3>
          </section>
        </template>
      </div>
    </template>
    <template v-else-if="APIPage == 4">
      <div class="logs">
        <template v-if="promoStats != null && promoStats.length > 0">
          <p style="color: #ccc; font-size: 15px; font-weight: bold;">Реферальная ссылка: <a>http://{{ serverTypeLink[this.promoStats[0].serverType] }}/application/controllers/cpromo.php?yt={{ this.promoStats[0].promoname }}&sT={{ this.promoStats[0].serverType }}&s={{ this.promoStats[0].server }}</a></p>
          <p style="color: #ccc; font-size: 15px; font-weight: bold;">Сервер: {{ serverTypeName[this.promoStats[0].serverType] }}.<br>Номер сервера: {{ this.promoStats[0].server }}</p>
          <br>
          <div class="table-container">
            <table>
              <tr>
                <th>Дата</th>
                <th>Переходов</th>
                <th>Скачиваний</th>
                <th>Зарегистрировано</th>
                <th>Отыграно часов</th>
              </tr>
              <tr>
                <td>Всего:</td>
                <td>{{ totalPromotions.totalTransitions }}</td>
                <td>{{ totalPromotions.totalDownloads }}</td>
                <td>{{ totalPromotions.totalRegistered }}</td>
                <td>{{ totalPromotions.totalPlayed }}</td>
              </tr>
              <tr>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
              </tr>
              <tr v-for="promo in promoStats" :key="promo.ID">
                <td>{{ promo.date }}</td>
                <td>{{ promo.transitions }}</td>
                <td>{{ promo.downloads }}</td>
                <td>{{ promo.registered }}</td>
                <td>{{ Math.round(promo.hoursPlayed / 60) }}</td>
              </tr>
            </table>
          </div>
        </template>
        <template v-else>
          <section>
            <h3>Для данного промокода пока нет статистики!</h3>
          </section>
        </template>
      </div>
    </template>
    <template v-else-if="APIPage == 5">
      <div class="logs">
        <template v-if="promoStats != null && promoStats.length > 0">
          <p style="color: #ccc; font-size: 15px; font-weight: bold;">Статистика всех промокодов, со всех проектов и серверов за один месяц.<br>Дата: <a>{{ this.params.date }}</a></p>
          <br>
          <div class="table-container">
            <table>
              <tr>
                <th>Проект(сервер)</th>
                <th>Промокод</th>
                <th>Переходов</th>
                <th>Скачиваний</th>
                <th>Зарегистрировано</th>
                <th>Отыграно часов</th>
              </tr>
              <tr>
                <td>Всего:</td>
                <td>-</td>
                <td>{{ totalPromotions.totalTransitions }}</td>
                <td>{{ totalPromotions.totalDownloads }}</td>
                <td>{{ totalPromotions.totalRegistered }}</td>
                <td>{{ totalPromotions.totalPlayed }}</td>
              </tr>
              <tr>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
              </tr>
              <tr v-for="promo in promoStats" :key="promo.ID">
                <td>{{ serverTypeName[promo.serverType] }}({{ promo.server }})</td>
                <td>{{ promo.promoname }}</td>
                <td>{{ promo.transitions }}</td>
                <td>{{ promo.downloads }}</td>
                <td>{{ promo.registered }}</td>
                <td>{{ Math.round(promo.hoursPlayed / 60) }}</td>
              </tr>
            </table>
          </div>
        </template>
        <template v-else>
          <section>
            <h3>Для данного промокода пока нет статистики!</h3>
          </section>
        </template>
      </div>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
import config from '@/config/config.js'
import Header from '@/components/includes/Header'

export default {
  components: {
    Header
  },
  data () {
    return {
      APIPage: null,
      promoStats: null,
      params: this.$route.query,
      // Promostats
      serverTypeLink: ['santrope-rp.com', 'bh-rp.com'],
      serverTypeName: ['SanTrope', 'Barvikha'],
      transitions: 0,
      downloads: 0,
      registered: 0,
      played: 0
    }
  },
  mounted () {
    this.Router()
  },
  methods: {
    async Router () {
      var method = this.params.method
      switch (method) {
        case 'ipdata': {
          this.APIPage = 1
          break
        }
        case 'stats': {
          const response = await axios({
            url: config.config.serverURL + '/promo/stats',
            method: 'POST',
            data: {
              ID: this.params.ID
            }
          })
          this.promoStats = response.data
          this.APIPage = 2
          break
        }
        case 'findDayStats': {
          const response = await axios({
            url: config.config.serverURL + '/promo/fd-stats',
            method: 'POST',
            data: {
              date: this.params.date
            }
          })
          this.promoStats = response.data
          this.APIPage = 3
          break
        }
        case 'findMonthStats': {
          const response = await axios({
            url: config.config.serverURL + '/promo/fm-stats',
            method: 'POST',
            data: {
              promo: this.params.promo,
              date: this.params.date
            }
          })
          this.promoStats = response.data
          this.APIPage = 4
          break
        }
        case 'findTMonthStats': {
          const response = await axios({
            url: config.config.serverURL + '/promo/ftm-stats',
            method: 'POST',
            data: {
              date: this.params.date
            }
          })
          this.promoStats = response.data
          this.APIPage = 5
          break
        }
        case 'delete-promo': {
          await axios({
            url: config.config.serverURL + '/promo/delete-promo',
            method: 'POST',
            data: {
              ID: this.params.ID
            }
          })
          this.$router.push('/' + this.params.redirect_url)
          break
        }
        default: {
          this.$router.push('/')
          break
        }
      }
    }
  },
  computed: {
    totalPromotions () {
      const accumulator = {
        totalDownloads: 0,
        totalPlayed: 0,
        totalRegistered: 0,
        totalTransitions: 0
      }
      // sum each promotion variable
      this.promoStats.forEach(promotion => {
        accumulator.totalDownloads += promotion.downloads
        accumulator.totalPlayed += Math.round(promotion.hoursPlayed / 60)
        accumulator.totalRegistered += promotion.registered
        accumulator.totalTransitions += promotion.transitions
      })
      return accumulator
    }
  }
}
</script>



// WEBPACK FOOTER //
// API.vue