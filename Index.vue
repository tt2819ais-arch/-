<template>
  <div class="index">
    <Header />
    <form @submit.prevent="sendLogsSearchData">
      <div class="params" style="background: #232428">
        <div class="params-column">
          <div class="params-column_row">
            <p style="color: #ccc;">Дата от:</p>
            <input type="date" v-model="dateFrom" style="background: #413F43; color: #ccc;">
          </div>
          <div class="params-column_row">
            <p style="color: #ccc;">Дата до:</p>
            <input type="date" v-model="dateTo" style="background: #413F43; color: #ccc;">
          </div>
        </div>
        <div class="params-column">
          <div class="params-column_row">
            <p style="color: #ccc;">ID аккаунта:</p>
            <input type="number" v-model="accid" style="background: #413F43; color: #ccc;">
          </div>
          <div class="params-column_row">
            <p style="color: #ccc;">ID предмета:</p>
            <input type="number" v-model="itemid" style="background: #413F43; color: #ccc;">
          </div>
        </div>
        <div class="params-column">
          <div class="params-column_row">
            <p style="color: #ccc;">ID действия:</p>
            <input type="number" v-model="actionid" style="background: #413F43; color: #ccc;">
          </div>
          <div class="params-column_row">
            <p style="color: #ccc;">Сумма:</p>
            <input type="number" v-model="summ" style="background: #413F43; color: #ccc;">
          </div>
        </div>
        <div class="params-column">
          <div class="params-column_row">
            <p style="color: #ccc;">IP адрес:</p>
            <input type="text" v-model="ip" style="background: #413F43; color: #ccc;">
          </div>
          <div class="params-column_row">
            <p style="color: #ccc;">Сортировать:</p>
            <select v-model="sort" style="background: #413F43; color: #ccc;">
              <option :value="null">По дате (убывание)</option>
              <option value="`id` ASC">По дате (возрастание)</option>
              <option value="`count` DESC">По количеству предметов (убывание)</option>
              <option value="`count` ASC">По количеству предметов (возрастание)</option>
            </select>
          </div>
          <div class="params-column_row">
            <input type="submit" name="submit" value="Поиск">
          </div>
        </div>
      </div>
    </form>
    <div class="logs">
      <template v-if="logsList && logsList.length > 0">
        <LogsFile v-bind:logsList="logsList" :key="uniqueVal"></LogsFile>
      </template>
      <template v-else>
        <h3>Пока в базе данных нет ещё логов!</h3>
      </template>
    </div>
    <form @submit.prevent="loadLogsSearchData">
      <div class="params" style="background: #232428">
        <div class="params-column_row">
          <input type="submit" name="submit" value="Загрузить ещё..">
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import config from '@/config/config.js'
import iH from '@/services/indexHandler'
import Header from '@/components/includes/Header'
import LogsFile from '@/components/includes/LogsTemplate'

export default {
  components: {
    Header,
    LogsFile
  },
  data () {
    return {
      logsList: null,
      //
      dateFrom: null,
      dateTo: null,
      accid: null,
      itemid: null,
      actionid: null,
      summ: null,
      ip: null,
      limit: 80,
      sort: null,
      page: 1,
      //
      uniqueVal: 0
    }
  },
  mounted () {
    this.searchForLogs()
  },
  methods: {
    async searchForLogs () {
      var params = this.$route.query
      var checkVar = false

      if (params.dateFrom === '' || params.dateFrom === undefined) {
        this.dateFrom = null
      } else {
        checkVar = true
        this.dateFrom = params.dateFrom
      }
      if (params.dateTo === '' || params.dateTo === undefined) {
        this.dateTo = null
      } else {
        checkVar = true
        this.dateTo = params.dateTo
      }
      if (params.accid === '' || params.accid === undefined) {
        this.accid = null
      } else {
        checkVar = true
        this.accid = params.accid
      }
      if (params.itemid === '' || params.itemid === undefined) {
        this.itemid = null
      } else {
        checkVar = true
        this.itemid = params.itemid
      }
      if (params.actionid === '' || params.actionid === undefined) {
        this.actionid = null
      } else {
        checkVar = true
        this.actionid = params.actionid
      }
      if (params.summ === '' || params.summ === undefined) {
        this.summ = null
      } else {
        checkVar = true
        this.summ = params.summ
      }
      if (params.ip === '' || params.ip === undefined) {
        this.ip = null
      } else {
        checkVar = true
        this.ip = params.ip
      }
      if (params.sort === '' || params.sort === undefined) {
        this.sort = null
      } else {
        checkVar = true
        this.sort = params.sort
      }
      if (checkVar === true) {
        await this.sendLogsSearchData()
      } else {
        const response = await iH.getAllLogs()
        this.logsList = response.data
      }
    },
    async sendLogsSearchData () {
        this.page = 1
        this.limit = 80

        const postData = {
            dateFrom: this.dateFrom,
            dateTo: this.dateTo,
            accID: this.accid,
            itemID: this.itemid,
            actionID: this.actionid,
            amount: this.summ,
            IP: this.ip,
            Limit: this.limit * this.page,
            Sort: this.sort
        };

        const conf = {
            withCredentials: true,
        };

        const response = await axios.post(
            config.config.serverURL + '/searchEngine',
            postData,
            conf
        );
        this.logsList = response.data
        this.uniqueVal += 1
    },
    async loadLogsSearchData () {
        this.page += 1

        const postData = {
            dateFrom: this.dateFrom,
            dateTo: this.dateTo,
            accID: this.accid,
            itemID: this.itemid,
            actionID: this.actionid,
            amount: this.summ,
            IP: this.ip,
            Limit: (this.limit * this.page),
            Sort: this.sort
        };

        const conf = {
            // Установите опцию 'withCredentials' в true
            withCredentials: true,
        };

        const response = await axios.post(
            config.config.serverURL + '/searchEngine',
            postData,
            conf
        );
        this.logsList = response.data
    }
  }
}
</script>



// WEBPACK FOOTER //
// Index.vue