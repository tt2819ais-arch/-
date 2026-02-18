<template>
  <div class="promocodes">
    <Header />
    <div class="content">
      <div class="content-items">
        <div class="content-items_add" style="margin-top: 0;">
          <router-link to="/promo/create">+</router-link>
        </div>
        <div class="content-items_col">
          <section>
            <span>#</span>
            <p>Поиск статистики за день</p>
          </section>
          <router-link to="/promo/fd-stats">Поиск</router-link>
        </div>
        <div class="content-items_col">
          <section>
            <span>#</span>
            <p>Поиск статистики за месяц</p>
          </section>
          <router-link to="/promo/fm-stats">Поиск</router-link>
        </div>
        <div class="content-items_col">
          <section>
            <span>#</span>
            <p>Поиск общей статистики за месяц</p>
          </section>
          <router-link to="/promo/ftm-stats">Поиск</router-link>
        </div>
        <div class="content-items_col">
          <section>
            <span>#</span>
            <p>Промокоды Сантропа</p>
          </section>
        </div>
        <template v-if="promoCodes != null">
          <div v-for="(promo, i) in promoCodes" :key="'S'+ i">
            <div v-if="promo.ServerType == 0" class="content-items_col">
              <section>
                <span>#{{promo.Server}}</span>
                <p>Промокод: "{{promo.Name}}"</p>
              </section>
              <a :href="`${promo.Link}`" style="background: #EA363F;">Перейти</a>
              <router-link :to="`API?method=stats&ID=${promo.ID}&promoCode=${promo.promoname}&serverType=${promo.ServerType}&server=${promo.Server}`" style="background: #EA363F;">Статистика</router-link>
              <router-link :to="`API?method=delete-promo&ID=${promo.ID}&redirect_url=promo`">Удалить</router-link>
            </div>
          </div>
        </template>
        <div class="content-items_col">
          <section>
            <span>#</span>
            <p>Промокоды Барвихи</p>
          </section>
        </div>
        <template v-if="promoCodes != null">
          <div v-for="(promo, i) in promoCodes" :key="'B'+ i">
            <div v-if="promo.ServerType == 1" class="content-items_col">
              <section>
                <span>#{{promo.Server}}</span>
                <p>Промокод: "{{promo.Name}}"</p>
              </section>
              <a :href="`${promo.Link}`" style="background: #EA363F;">Перейти</a>
              <router-link :to="`API?method=stats&ID=${promo.ID}&promoCode=${promo.Name}&serverType=${promo.ServerType}&server=${promo.Server}`" style="background: #EA363F;">Статистика</router-link>
              <router-link :to="`API?method=delete-promo&ID=${promo.ID}&redirect_url=promo`">Удалить</router-link>
            </div>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '@/components/includes/Header'
import pH from '@/services/promoHandler'
export default {
  components: {
    Header
  },
  data () {
    return {
      promoCodes: null
    }
  },
  mounted () {
    this.loadPromoList()
  },
  methods: {
    async loadPromoList () {
      const response = await pH.loadPromoList()
      this.promoCodes = response.data
    }
  }
}
</script>



// WEBPACK FOOTER //
// Promocodes.vue