<template>
  <div class="logs-file">
    <template v-for="log in logsList">
      <!--  -->
      <template v-if="log.d_id == 1">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`id\` DESC`"
              >{{ log.a_id_from }}</a
            >) вошел IP:<a :href="`API?method=ipdata&&ip=${log.ip}`">{{
              log.ip
            }}</a>
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`id\` DESC`"
              >{{ log.a_id_from }}</a
            >) вышел IP:<a :href="`API?method=ipdata&ip=${log.ip}`">{{
              log.ip
            }}</a>
            (сессия: {{ log.note }} сек; AFK: {{ log.count }} сек)
          </p>
        </template>
        <template v-else-if="log.o_id == 3">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`id\` DESC`"
              >{{ log.a_id_from }}</a
            >) неудачный вход IP:<a :href="`API?method=ipdata&ip=${log.ip}`">{{
              log.ip
            }}</a>
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 2">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: [{{ log.count }}] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) принял {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: [{{ log.count }}] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) уволил {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) (c {{ log.note.split("|")[0] }} ранга). Причина:
            {{ log.note.split("|")[1] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 3">
          <p :key="log.id">
            {{ log.date }}: [{{ log.count }}] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) сменил ранг {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) (с {{ log.note.split("|")[0] }} на
            {{ log.note.split("|")[1] }} ранг). Ранг его:
            {{ log.note.split("|")[0] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 4">
          <p :key="log.id">
            {{ log.date }}: [{{ log.count }}] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выдал выговор {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) ({{ log.note.split("|")[0] }} из 3). Причина:
            {{ log.note.split("|")[1] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 5">
          <p :key="log.id">
            {{ log.date }}: [{{ log.count }}] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) очистил черный список
          </p>
        </template>
        <template v-else-if="log.o_id == 6">
          <p :key="log.id">
            {{ log.date }}: [{{ log.count }}] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) добавил в ЧС {{ log.a_name_to }} (<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >)
          </p>
        </template>
        <template v-else-if="log.o_id == 7">
          <p :key="log.id">
            {{ log.date }}: [{{ log.count }}] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) вычеркнул из ЧС {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >)
          </p>
        </template>
        <template v-else-if="log.o_id == 8">
          <p :key="log.id">
            {{ log.date }}: [{{ log.count }}] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) снял с банка $${log.count}}
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 3">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) назначил на пост администратора {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >). ({{ log.note.split("|")[0] }} уровень)
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) снял с поста администратора {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 3">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) назначил на пост лидера {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >). ({{ log.count }} фракции)
          </p>
        </template>
        <template v-else-if="log.o_id == 4">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) снял с поста лидера {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 5">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) ответил игроку {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).Ответ: {{ log.note.split("|")[0] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 6">
          <template v-if="rank >= 1">
            <p :key="log.id">
              {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
                :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
                >{{ log.a_id_from }}</a
              >) удалил тикет {{ log.a_name_to }}(<a
                :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
                >{{ log.a_id_to }}</a
              >).
            </p>
          </template>
        </template>
        <template v-else-if="log.o_id == 7">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) телепортировался к игроку {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 8">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) телепортировал к себе {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 9">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выдал мут {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >). На {{ log.note.split("|")[0] }} минут. Причина:
            {{ log.note.split("|")[1] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 10">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) снял мут с {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 11">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) кикнул {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >). Причина: {{ log.note.split("|")[0] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 12">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выдал варн {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) ({{ log.note.split("|")[0] }} из 3). Причина:
            {{ log.note.split("|")[1] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 13">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) забанил {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >). На {{ log.note.split("|")[0] }} дней. Причина:
            {{ log.note.split("|")[1] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 14">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) разбанил {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 15">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) заблокировал IP
            <a :href="`API?method=ipdata&ip=${log.ip}`">{{ log.ip }}</a
            >). Причина: {{ log.note }}
          </p>
        </template>
        <template v-else-if="log.o_id == 16">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) разблокировал IP
            <a :href="`API?method=ipdata&ip=${log.ip}`">{{ log.ip }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 17">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) посадил в присон {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >). (На {{ log.note.split("|")[0] }} минут). Причина:
            {{ log.note.split("|")[1] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 18">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выпустил из присона {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 19">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выдал денег {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >). ({{ log.note.split("|")[0] }})
          </p>
        </template>
        <template v-else-if="log.o_id == 20">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выдал донат {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >). ({{ log.note.split("|")[0] }})
          </p>
        </template>
        <template v-else-if="log.o_id == 21">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) удалил аккаунт {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 22">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) заблокировал ПК {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 23">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выдал лицензию {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).(id: {{ log.note.split("|")[0] }})
          </p>
        </template>
        <template v-else-if="log.o_id == 24">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) изменил пароль {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 25">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) отключил GA {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 26">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) уволил из фракции {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 27">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) сменил ник {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 28">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) сменил скин {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >).
          </p>
        </template>
        <template v-else-if="log.o_id == 34">
          <p :key="log.id">
            {{ log.date }}: [ADM] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) назначил на зону #{{ log.a_id_to }} семью №{{ log.count }}
            {{ log.note }}
          </p>
        </template>
        <template v-else-if="log.o_id == 33">
          <p :key="log.id">
            {{ log.date }}: [ADM] Онлайн администраторов:
            {{ log.note.split("|")[0] }}шт. В AFK:
            {{ log.note.split("|")[1] }} шт. В спеке:
            {{ log.note.split("|")[2] }}. Кол-во тикетов:
            {{ log.note.split("|")[3] }}
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 4">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) перевел на банк. счет {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) деньги {{ log.count }} (с {{ log.note.split("|")[0] }} на
            {{ log.note.split("|")[1] }})
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) передал {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) деньги {{ log.count }}
          </p>
        </template>
      </template>
      <!--  -->
      <!--  -->
      <template v-else-if="log.d_id == 38">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) подвез {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) за {{ log.count1 }} руб
          </p>
        </template>
        <template v-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) получил чаевые от {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) в размере {{ log.count1 }} руб
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 5">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил дом №<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >. Стоимость: {{ log.count }}
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил бизнес №<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >. Стоимость: {{ log.count }}
          </p>
        </template>
        <template v-else-if="log.o_id == 3">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил транспорт модель {{ log.a_id_to }}. Стоимость:
            {{ log.count }}
          </p>
        </template>
        <template v-else-if="log.o_id == 4">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) продал дом №${{ log.count }} {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) за {{ log.note.split("|")[0] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 5">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) продал бизнес №${{ log.count }} {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) за {{ log.note.split("|")[0] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 6">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) продал транспорт. Модель: {{ log.count }} {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) за {{ log.note.split("|")[0] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 8">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) закупил товаров в бизнес №{{ log.a_id_to }} на
            {{ log.count }} руб.
          </p>
        </template>
        <template v-else-if="log.o_id == 9">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) оплатил бизнес №{{ log.a_id_to }} на {{ log.note }} дней за
            {{ log.count }} руб.
          </p>
        </template>
        <template v-else-if="log.o_id == 10">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) пополнил/снял с баланса бизнеса №{{ log.a_id_to }}
            {{ log.count }} руб. Остаток {{ log.note }} руб.
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 6">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выиграл в казино {{ log.count }}
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) проиграл в казино {{ log.count }}
          </p>
        </template>
        <template v-else-if="log.o_id == 3">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выиграл {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) {{ log.count }} в орел и решку
          </p>
        </template>
      </template>
      <template v-else-if="log.d_id == 33">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выиграл в казино {{ log.count }}
            Игроки:
            {{ log.note.split("|")[0] }} {{ log.note.split("|")[1] }},
            {{ log.note.split("|")[2] }} {{ log.note.split("|")[3] }},
            {{ log.note.split("|")[4] }} {{ log.note.split("|")[5] }},
            {{ log.note.split("|")[6] }} {{ log.note.split("|")[7] }},
            {{ log.note.split("|")[8] }} {{ log.note.split("|")[9] }}
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 7">
        <template v-if="log.o_id == 1">
          <!-- {% set value = log.note.split('|')%}
          {% set valuesArray = []>
          {% for i in range(0, value | length)>
            <template v-if='valuesArray.insert(i, (value[i] | int))'>
            </template>
          {% endfor>
          <!- <p :key='log.id'>{{log.date}}: {{log.a_name_from}}(<a :href='`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`'>{{log.a_id_from}}</a>) купил 1 ({{log.count}} шт.). за {{log.note.split('|')[1]}} у {{log.a_name_to}}(<a :href='`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`'>{{log.a_id_to}}</a>)</p> -->
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 8">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) сменил ник на {{ log.note.split("|")[0] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 3">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) {{ items_array[log.count] }} Было: {{ log.note.split("|")[0] }}.
            Стало: {{ log.note.split("|")[1] }}. Итог:
            {{ log.note.split("|")[2] }} CT {{ log.count }}
          </p>
        </template>
        <template v-else-if="log.o_id == 4">
          <template v-if="log.count == 93">
            <!-- {% set value = log.note.split('|')%}
            {% set valuesArray = []>
            {% for i in range(0, value | length)
              <template v-if='valuesArray.insert(i, (value[i] | int))'>
              </template>
            {% endfor> -->
            <p :key="log.id">
              {{ log.date }}: {{ log.a_name_from }}(<a
                :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
                >{{ log.a_id_from }}</a
              >) купил у {{ log.a_name_to }}(<a
                :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
                >{{ log.a_id_to }}</a
              >) {{ type_inv[valuesArray[3]] }}({{
                log.note.split("|")[4]
              }}
              шт.). Было: {{ log.note.split("|")[0] }}. Стало:
              {{ log.note.split("|")[1] }}. Итог: {{ log.note.split("|")[2] }}
            </p>
          </template>
          <template v-else>
            <p :key="log.id">
              {{ log.date }}: {{ log.a_name_from }}(<a
                :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
                >{{ log.a_id_from }}</a
              >) {{ items_array[log.count] }} {{ log.a_name_to }}(<a
                :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
                >{{ log.a_id_to }}</a
              >) Было: {{ log.note.split("|")[0] }}. Стало:
              {{ log.note.split("|")[1] }}. Итог: {{ log.note.split("|")[2] }}
            </p>
          </template>
        </template>
        <template v-else-if="log.o_id == 5">
          <p :key="log.id">
            {{ log.date }}: Manager {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выдал {{ log.count }} {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >)
          </p>
        </template>
        <template v-else-if="log.o_id == 6">
          <p :key="log.id">
            {{ log.date }}: Manager {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выдал в оффе {{ log.count }} {{ log.a_name_to }}
          </p>
        </template>
        <template v-else-if="log.o_id == 7">
          <p :key="log.id">
            {{ log.date }}: Manager {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выдал ютуберку {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) на {{ log.count }} часов
          </p>
        </template>
        <template v-else-if="log.o_id == 8">
          <p :key="log.id">
            {{ log.date }}: Manager {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) создал промокод {{ log.note.split("|")[0] }}
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 9">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выиграл в казино {{ log.count }}
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) проиграл в казино {{ log.count }}
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 10">
        <template v-if="log.o_id == 1">
          <!-- {% set value = log.note.split('|')%} -->
          <!-- {% set valuesArray = []> -->
          <!-- {% for i in range(0, value | length)> -->
          <!-- <template v-if='valuesArray.insert(i, (value[i] | int))> </template> -->
          <!-- {% endfor> -->
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил контейнер {{ transfer[valuesArray[0]] }} ({{
              type_cont[valuesArray[1]]
            }}) Цена: {{ valuesArray[2] }} Итог: {{ valuesArray[3] }} Госс:
            {{ valuesArray[4] }}
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 11">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: Бизнес №<a
              :href="`/?&accid=${log.count}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.count }}</a
            >
            был передан государству. Причина: {{ log.note.split("|")[0] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: На бизнесе №<a
              :href="`/?&accid=${log.count}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.count }}</a
            >
            был изменен налог. Было: {{ log.note.split("|")[0] }}. Стало:
            {{ log.note.split("|")[1] }}. Итог: {{ log.note.split("|")[2] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 3">
          <p :key="log.id">
            {{ log.date }}: В бизнесе №<a
              :href="`/?&accid=${log.count}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.count }}</a
            >
            было изменено кол-во продуктов. Было: {{ log.note.split("|")[0] }}.
            Стало: {{ log.note.split("|")[1] }}. Итог:
            {{ log.note.split("|")[2] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 4">
          <p :key="log.id">
            {{ log.date }}: Бизнес №<a
              :href="`/?&accid=${log.count}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.count }}</a
            >
            достиг $0 налога
          </p>
        </template>
        <template v-else-if="log.o_id == 5">
          <p :key="log.id">
            {{ log.date }}: Бизнес №<a
              :href="`/?&accid=${log.count}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.count }}</a
            >
            достиг менее 50-ти продуктов
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 12">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) произвел действие в обменнике ( {{ log.note.split("|")[0] }} |
            {{ log.note.split("|")[1] }} | {{ log.note.split("|")[2] }} )
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 13">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) повысил уровень EventPass до {{ log.note.split("|")[0] }}ур. Тип
            приза:{{ log.note.split("|")[1] }}. Идентификатор:{{
              log.note.split("|")[2]
            }}
            )
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 22">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил номер '{{ log.note.split("|")[0] }}'. Тип номера:
            {{ log.count }}. Цена:{{ log.a_id_to }} руб.
          </p>
        </template>
        <template v-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) обменял {{ log.note }} с {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) Доплата {{ log.count }} руб.
          </p>
        </template>
        <template v-if="log.o_id == 4">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) продал {{ log.note }} игроку {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) Цена {{ log.count }} руб.
          </p>
        </template>
        <template v-if="log.o_id == 3">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) продал номер '{{ log.note.split("|")[0] }}'. Тип номера:
            {{ log.count }}. Цена:{{ log.a_id_to }} руб.
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 23">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) продал семью '{{ log.note.split("|")[0] }}' №{{
              log.count
            }}
            игроку {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) Цена {{ log.note.split("|")[1] }} руб.
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 14">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выполнил квест №{{ log.count }}
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 15">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) {{ security_array[log.count] }}
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 17">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: Онлайн на сервере: {{ log.note.split("|")[0] }}.
            Пиковый онлайн: {{ log.note.split("|")[1] }}
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 19">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: Статистика контейнеров | Забрали:
            {{ log.note.split("|")[0] }}. Отдали: {{ log.note.split("|")[1] }}
          </p>
        </template>
      </template>
      <!--  -->
      <template v-else-if="log.d_id == 20">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: Дом №{{ log.count }}. был передан государству за
            неуплату налогов
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: Дом №{{ log.count }}. был оплачен на
            {{ log.note.split("|")[2] }} часов. Было
            {{ log.note.split("|")[0] }}. Стало {{ log.note.split("|")[1] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 3">
          <p :key="log.id">
            {{ log.date }}: Дом №{{ log.count }}. оплачен на
            {{ log.note.split("|")[0] }} часов.
          </p>
        </template>
      </template>
      <template v-else-if="log.d_id == 21">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) (|{{ log.note.split("|")[1] }}|{{ log.note.split("|")[2] }}|{{
              log.note.split("|")[3]
            }}|{{ log.note.split("|")[4] }}|{{ log.note.split("|")[5] }}|{{
              log.note.split("|")[6]
            }}|{{ log.note.split("|")[7] }}|{{ log.note.split("|")[8] }}|{{
              log.note.split("|")[9]
            }}|{{ log.note.split("|")[10] }}|{{ log.note.split("|")[11] }}|{{
              log.note.split("|")[12]
            }}|{{ log.note.split("|")[13] }}|{{ log.note.split("|")[14] }}|{{
              log.note.split("|")[15]
            }}|{{ log.note.split("|")[16] }}|{{ log.note.split("|")[17] }}|{{
              log.note.split("|")[18]
            }}|{{ log.note.split("|")[19] }}|{{ log.note.split("|")[20] }}|{{
              log.note.split("|")[21]
            }}|) обменялся с {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) (|{{ log.note.split("|")[22] }}|{{ log.note.split("|")[23] }}|{{
              log.note.split("|")[24]
            }}|{{ log.note.split("|")[25] }}|{{ log.note.split("|")[26] }}|{{
              log.note.split("|")[27]
            }}|{{ log.note.split("|")[28] }}|{{ log.note.split("|")[29] }}|{{
              log.note.split("|")[30]
            }}|{{ log.note.split("|")[31] }}|{{ log.note.split("|")[32] }}|{{
              log.note.split("|")[33]
            }}|{{ log.note.split("|")[34] }}|{{ log.note.split("|")[35] }}|{{
              log.note.split("|")[36]
            }}|{{ log.note.split("|")[37] }}|{{ log.note.split("|")[38] }}|{{
              log.note.split("|")[39]
            }}|{{ log.note.split("|")[40] }}|{{ log.note.split("|")[41] }}|{{
              log.note.split("|")[42]
            }}|)
          </p>
        </template>
      </template>
      <template v-else-if="log.d_id == 24">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: У семьи {{ log.note }} №{{ log.count }} слетел
            особняк №{{ log.a_id_to }} в госс (семья слетела)
          </p>
        </template>
        <template v-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил особняк №{{ log.a_id_to }} для семьи {{ log.note }} №{{
              log.count
            }}
          </p>
        </template>
        <template v-if="log.o_id == 3">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) продал особняк №{{ log.a_id_to }} семьи {{ log.note }} №{{
              log.count
            }}
          </p>
        </template>
      </template>
      <template v-else-if="log.d_id == 25">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил {{ log.note }} за {{ log.count }} яиц
          </p>
        </template>
        <template v-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) обменял {{ log.a_id_to }} яиц на {{ log.count }} руб
          </p>
        </template>
      </template>
      <template v-else-if="log.d_id == 26">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выиграл аукцион за дом №{{ log.count }} Цена:
            {{ log.a_id_to }} руб
          </p>
        </template>
        <template v-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выиграл аукцион за бизнес №{{ log.count }} Цена:
            {{ log.a_id_to }} руб
          </p>
        </template>
      </template>
      <template v-else-if="log.d_id == 29">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купить тюнинг группа: {{ log.note.split("|")[3] }} деталь:
            {{ log.note.split("|")[4] }} Цена:
            {{ log.note.split("|")[2] }} Денег осталось:
            {{ log.note.split("|")[1] }}
          </p>
        </template>
      </template>
      <template v-else-if="log.d_id == 28">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            <template v-if="log.count == -1">
              {{ log.date }}: {{ log.a_name_from }}(<a
                :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
                >{{ log.a_id_from }}</a
              >) положил на осн. банк счет {{ log.note.split("|")[5] }} руб.
              (РБ: {{ log.note.split("|")[0] }} р., РС:
              {{ log.note.split("|")[1] }} р. / ББ:
              {{ log.note.split("|")[3] }} р., БС:
              {{ log.note.split("|")[4] }} р.)
            </template>
            <template v-if="log.count != -1">
              {{ log.date }}: {{ log.a_name_from }}(<a
                :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
                >{{ log.a_id_from }}</a
              >) положил на счет №{{ log.count }}
              {{ log.note.split("|")[5] }} руб. (РБ:
              {{ log.note.split("|")[0] }} р., РС:
              {{ log.note.split("|")[1] }} р. / ББ:
              {{ log.note.split("|")[3] }} р., БС:
              {{ log.note.split("|")[4] }} р.)
            </template>
          </p>
        </template>
        <template v-if="log.o_id == 2">
          <p :key="log.id">
            <template v-if="log.count == -1">
              {{ log.date }}: {{ log.a_name_from }}(<a
                :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
                >{{ log.a_id_from }}</a
              >) снял с осн. банк счет {{ log.note.split("|")[5] }} руб. (РБ:
              {{ log.note.split("|")[0] }} р., РС:
              {{ log.note.split("|")[1] }} р. / ББ:
              {{ log.note.split("|")[3] }} р., БС:
              {{ log.note.split("|")[4] }} р.)
            </template>
            <template v-if="log.count != -1">
              {{ log.date }}: {{ log.a_name_from }}(<a
                :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
                >{{ log.a_id_from }}</a
              >) снял со счета №{{ log.count }}
              {{ log.note.split("|")[5] }} руб. (РБ:
              {{ log.note.split("|")[0] }} р., РС:
              {{ log.note.split("|")[1] }} р. / ББ:
              {{ log.note.split("|")[3] }} р., БС:
              {{ log.note.split("|")[4] }} р.)
            </template>
          </p>
        </template>
        <template v-if="log.o_id == 3">
          <p :key="log.id">
            <template v-if="log.count == -1">
              {{ log.date }}: {{ log.a_name_from }}(<a
                :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
                >{{ log.a_id_from }}</a
              >) положил на счет моб. с осн. банк счета
              {{ log.note.split("|")[5] }} руб. (МБ:
              {{ log.note.split("|")[0] }} р., МС:
              {{ log.note.split("|")[1] }} р. / ББ:
              {{ log.note.split("|")[3] }} р., БС:
              {{ log.note.split("|")[4] }} р.)
            </template>
            <template v-if="log.count != -1">
              {{ log.date }}: {{ log.a_name_from }}(<a
                :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
                >{{ log.a_id_from }}</a
              >) положил на счет моб. со счета №{{ log.count }}
              {{ log.note.split("|")[5] }} руб. (МБ:
              {{ log.note.split("|")[0] }} р., МС:
              {{ log.note.split("|")[1] }} р. / ББ:
              {{ log.note.split("|")[3] }} р., БС:
              {{ log.note.split("|")[4] }} р.)
            </template>
          </p>
        </template>
        <template v-if="log.o_id == 4">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) перевел со счета №{{ log.count }} на счет №{{ log.a_id_to }}
            {{ log.note.split("|")[5] }} руб. (ПБ:
            {{ log.note.split("|")[0] }} р., ПС: {{ log.note.split("|")[1] }} р.
            / СБ: {{ log.note.split("|")[3] }} р., СС:
            {{ log.note.split("|")[4] }} р.)
          </p>
        </template>
        <template v-if="log.o_id == 5">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) перевел со счета №{{ log.count }} на счет №{{ log.a_id_to }} Номер аккаунта: <a
              :href="`/?&accid=${log.note.split('|')[6]}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.note.split("|")[6] }}</a
            > {{ log.note.split("|")[5] }} руб. (ПБ:
            {{ log.note.split("|")[0] }} р., ПС: {{ log.note.split("|")[1] }} р.
            / СБ: {{ log.note.split("|")[3] }} р., СС:
            {{ log.note.split("|")[4] }} р.)
          </p>
        </template>
      </template>
      <template v-else-if="log.d_id == 37">
        <p :key="log.id">
          {{ log.date }}: {{ log.a_name_from }}(<a
            :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
            >{{ log.a_id_from }}</a
          >) открыл контейнер за {{ log.count2 }} конт {{ log.count }}
          {{ log.count1 }} госс {{ log.count3 }} выпало на {{ log.a_id_to }}
        </p>
      </template>
      <template v-else-if="log.d_id == 27">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) продал сим-карту {{ log.count }} игроку {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) Цена {{ log.note }} руб.
          </p>
        </template>
      </template>
      <template v-else-if="log.d_id == 30">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил одежду №{{ log.count2 }} Цена {{ log.count }} руб. Цена без
            скидки {{ log.count1 }} руб.
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил одежду №{{ log.count1 }} у {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) Цена {{ log.count }} руб.
          </p>
        </template>
      </template>
      <template v-else-if="log.d_id == 31">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил в лавке {{ type_inv[log.count] }} у {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) Купил за {{ log.count1 }} руб. Продавец получил
            {{ log.count2 }} руб.
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил {{ type_inv[log.count] }} у {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) Купил за {{ log.count1 }} руб. Продавец получил
            {{ log.count2 }} руб.
          </p>
        </template>
      </template>
      <template v-else-if="log.d_id == 35">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) выиграл дуэль у {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) и выиграл {{ log.count }} руб.
          </p>
        </template>
      </template>
      <template v-else-if="log.d_id == 32">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) устроился на работу {{ job_array[log.count] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) уволился с работы {{ job_array[log.count] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 4">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) заработал на {{ tempjob_array[log.count] }} {{ log.count1 }} руб.
            Сессия: {{ log.count2 }} секунд
          </p>
        </template>
      </template>
      <template v-else-if="log.d_id == 34">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил танец {{ log.note }} за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил все танцы за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 3">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил {{ type_inv[log.count1] }} за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 4">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил стробоскопы за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 5">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил машину ID:{{ log.count1 }} за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 6">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил одежду ID:{{ log.count1 }} за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 7">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) сменил пол за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 8">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) сменил регион на {{ log.note }} за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 9">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил набор {{ type_nabor[log.count1] }} за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 10">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил набор лицензий за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 11">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил +1 опыт за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 12">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) очистил трудовую книгу за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 13">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил VIP за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 14">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) обменял {{ log.count }} Coins на {{ log.count1 }} руб
          </p>
        </template>
        <template v-else-if="log.o_id == 15">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) сменил возраст на {{ log.count1 }} лет за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 16">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) купил симкарту {{ log.count1 }} за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 17">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) сменил ник на {{ log.note }} за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 18">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) снял варн за {{ log.count }} Coins
          </p>
        </template>
        <template v-else-if="log.o_id == 19">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) пополнил баланс на {{ log.count }} Coins
          </p>
        </template>
      </template>
      <!--  -->
      <!--  -->
      <template v-else-if="log.d_id == 100">
        <template v-if="log.o_id == 1">
          <p :key="log.id">
            {{ log.date }}: [{{ log.count }}] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) сменил ранг {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) (с {{ log.note.split("|")[0] }} на
            {{ log.note.split("|")[1] }} ранг). Ранг его:
            {{ log.note.split("|")[2] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 2">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) продал дом №${{ log.count }} {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) за {{ log.note.split("|")[0] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 3">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) продал транспорт. Модель: {{ log.count }} {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) за {{ log.note.split("|")[0] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 4">
          <p :key="log.id">
            {{ log.date }}: {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) {{ log.count1 }} {{ log.count2 }} {{ log.count3 }} купил
            {{ type_inv[1] }} ({{ log.note.split("|")[0] }} шт.). за
            {{ log.note.split("|")[1] }} у {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >)
          </p>
        </template>
        <template v-else-if="log.o_id == 5">
          <p :key="log.id">
            {{ log.date }}: [{{ log.count }}] {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) уволил более 2-х {{ log.a_name_to }}(<a
              :href="`/?&accid=${log.a_id_to}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_to }}</a
            >) (c {{ log.note.split("|")[0] }} ранга). Причина:
            {{ log.note.split("|")[1] }}
          </p>
        </template>
        <template v-else-if="log.o_id == 6">
          <p :key="log.id">
            {{ log.date }}: У {{ log.a_name_from }}(<a
              :href="`/?&accid=${log.a_id_from}&itemid=&actionid=&summ=&ip=&sort=\`count\` ASC`"
              >{{ log.a_id_from }}</a
            >) {{ type_inv[log.count] }}({{ log.count }}) ({{
              log.note.split("|")[0]
            }}
            шт.).
          </p>
        </template>
      </template>
      <!--  -->
    </template>
  </div>
</template>

<script>
export default {
  props: ['logsList'],
  data () {
    return {
      type_inv: [
        'Пусто',
        'Наркотики',
        'Патроны',
        'Ед. оружия',
        'Семена',
        'Справочник',
        'Аптечка',
        'Рем. набор',
        'GPS трекер',
        'Веревка',
        'Маска',
        'Канистра',
        'Часы #1',
        'Часы #2',
        'Часы #3',
        'Часы #4',
        'Часы #5',
        'Часы #6',
        'Часы #7',
        'Часы #8',
        'Часы #9',
        'Часы #10',
        'Часы #11',
        'Часы #12',
        'Наушники #1',
        'Наушники #2',
        'Наушники #3',
        'Наушники #4',
        'Бандана #1',
        'Бандана #2',
        'Бандана #3',
        'Бандана #4',
        'Бандана #5',
        'Бандана #6',
        'Бандана #7',
        'Бандана #8',
        'Бандана #9',
        'Бандана #10',
        'Очки #1',
        'Очки #2',
        'Очки #3',
        'Очки #4',
        'Очки #5',
        'Очки #6',
        'Ошибка',
        'Ошибка',
        'Ошибка',
        'Очки #10',
        'Очки #11',
        'Очки #12',
        'Очки #13',
        'Очки #14',
        'Очки #15',
        'Очки #16',
        'Очки #17',
        'Очки #18',
        'Шапка #1',
        'Шапка #2',
        'Шапка #3',
        'Шапка #4',
        'Шапка #5',
        'Шапка #6',
        'Панама #1',
        'Панама #2',
        'Панама #3',
        'Кепка назад #1',
        'Кепка назад #2',
        'Кепка назад #3',
        'Кепка назад #4',
        'Кепка #1',
        'Кепка #2',
        'Кепка #3',
        'Кепка #4',
        'Кепка #5',
        'Кепка #6',
        'Кепка #7',
        'Кепка #8',
        'Каска #1',
        'Каска #2',
        'Каска #3',
        'Каска #4',
        'Каска #5',
        'Каска #6',
        'Парик #1',
        'Парик #2',
        'Берет #1',
        'Берет #2',
        'Берет #3',
        'Берет #4',
        'Берет #5',
        'Шляпа #1',
        'Шляпа #2',
        'Шляпа #3',
        'Шляпа #4',
        'Шляпа #5',
        'Рюкзак #1',
        'Рюкзак #2',
        'Рюкзак #3',
        'Шляпа #1',
        'Шляпа #2',
        'Шляпа #3',
        'Шляпа #4',
        'Шляпа #5',
        'Шляпа #6',
        'Бандана #10',
        'Бандана #11',
        'Бандана #12',
        'Бандана #13',
        'Бандана #14',
        'Усы #1',
        'Усы #2',
        'Гитара #1',
        'Гитара #2',
        'Гитара #3',
        'Ошибка',
        'Шапка Санты',
        'Ошибка',
        'Повязка на глаз',
        'Новогодний рюкзак #1',
        'Новогодний рюкзак #2',
        'Новогодний рюкзак #3',
        'Ошибка',
        'Новогодний рюкзак #5',
        'Елка',
        'Чемодан',
        'Монета',
        'Гриб',
        'Бумбокс',
        'Скейт',
        'Бронижелет',
        'Шлем',
        'Медицинский кейс',
        'Хокейная маска (З)',
        'Хокейная маска (К)',
        'Голова курицы',
        'Оранжевый желет',
        'Маска дьявола',
        'Строительная каска',
        'Голова сиджея',
        'Попугай',
        'Конопляный куст',
        'Шляпа мага',
        'Бензопила',
        'Конфета',
        'Маска Вендетты',
        'Маска Джейсона',
        'Окровавленная мачета',
        'Рука зомби',
        'Тыква',
        'Бинт',
        'Шины',
        'Аспирин',
        'Морфий',
        'Адреналин',
        'RC Bandit',
        'RC Baron',
        'RC Raider',
        'RC Goblin',
        'RC Tiger',
        'Рюкзак горный',
        'Борода санты',
        'Рюкзак олененок',
        'Рюкзак солдатик',
        'Сноуборд очки',
        'Маска медведь',
        'Шапка с легким паром',
        'Шапка ушанка',
        'Шапка санты',
        'Рога оленя',
        'Маска олененок',
        'Рюкзак камуфляжный',
        'Очки ридика',
        'Очки блатные',
        'Маска шут',
        'Маска конь',
        'Маска распиратор3',
        'Панама модник',
        'Маска распиратор',
        'Рюкзак скалолаз',
        'Маска распиратор2',
        'Маска хокейная',
        'Санки',
        'UFC пояс',
        'Наживка',
        'Наживка',
        'Наживка',
        'Маска POCO',
        'Маска STEVE',
        'Наушники JBL',
        'JBL EXTREM',
        'JBL BOOMBOX',
        'Маска от коронавируса',
        'Антисептик',
        'Георгиевская ленточка',
        'Гаечный ключ',
        'Трещётка',
        'Электро-болгарка',
        'Магнитофон',
        'Аудио-система',
        'Кепка SuperMen',
        'Кепка DG',
        'Кепка Drugs',
        'Кепка NY',
        'Панама B SHARK',
        'Панама Nike',
        'Панама Louis Vuitton',
        'Крест',
        'Бананка Louis Vuitton',
        'Бананка OFF-WHITE',
        'Бананка TNF',
        'Бананка TNF SUPREME',
        'Рюкзак Nike',
        'Рюкзак GUCCI',
        'Сумка Louis Vuitton',
        'Сумка Supreme',
        'Сумка Adidas',
        'Mono сумка OFF-WHITE',
        'Mono сумка GUCCI',
        'Mono сумка Louis Vuitton',
        'Маска Баба Яга',
        'Шляпа Ведьмы',
        'Метла',
        'Маска Денежный череп',
        'Тыква',
        'Семейная монета',
        'Рюкзак Новый год',
        'Рюкзак Знак дракона',
        'Сумка Новый год',
        'Киберпанк',
        'Маска волка',
        'Маска Светлых сил',
        'Маска Темной силы',
        'Новогодняя шапка',
        'Шарф',
        'Маска Панда',
        'Бомба',
        'Порох',
        'Скотч',
        'Часовой механизм',
        'Золото',
        'Бронза',
        'Аллюминий',
        'Брусок',
        'Дерево',
        'Камень',
        'Металл',
        'Титановая пластина',
        'Цепь',
        'Металлическая рама',
        'Шестерни',
        'Лопата',
        'Нож',
        'Велосипед',
        'АК 47',
        'Отбойник',
        'Шляпа Фермер',
        'Кислородный балон',
        'Кувалда',
        'Пасхальное яйцо',
        'Медаль ВОВ',
        'Пилотка ВОВ',
        'Маска Кролик'
      ],
      type_stcoins: [
        'выиграл в рулетке',
        'выдал админ',
        'купил уникальную монету',
        'купил транспорт',
        'купил одежду',
        'сменил пол',
        'купил номера на тс',
        'купил набор',
        'купил лицы',
        'купил EXP',
        'купил рулетку',
        'купил трудовую книгу',
        'купил вип',
        'обменял на бабки',
        'сменил возраст персонажа',
        'купил номер телефона',
        'сменил ник',
        'снял предупреждение',
        'рп квест',
        'начисление',
        'евент пасс'
      ],
      security_array: [
        'ошибка',
        'сбросил пароль',
        'сбросил аунтификатор',
        'подтвердил почту'
      ],
      type_nabor: [
        'ошибка',
        'Стартовый',
        'бизнесмен',
        'солидный',
        'золотой',
        'миллионер'
      ],
      tempjob_array: ['Шахта', 'Ферма', 'Развозчик пиццы', 'Завод', 'Водолаз'],
      job_array: [
        'Безработный',
        'Водитель автобуса',
        'Таксист',
        'Механик',
        'Дальнобойщик',
        'Развозчик продуктов',
        'Развозчик топлива',
        'Мореплаватель',
        'Вертолётчик',
        'Авиатор',
        'Уборщик улиц',
        'Перевозчик',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Безработный',
        'Таксопарк №1',
        'Таксопарк №2',
        'Безработный',
        'Безработный'
      ],
      transfer: ['AliExpress', 'EMS', 'FedEx', 'Amazon'],
      type_cont: ['Пром. товары', 'Транспорт', 'Error', 'Error'],
      items_array: [
        'получил запралату в порту',
        'выиграл дуэль',
        'получил зарплату на заводе',
        'получил зарплату на шахте',
        'получил зарплату на ферме',
        'получил зарплату администратора',
        'получил за бонусный промокод',
        'снял деньги с лавки',
        'возврат за регистрацию на МП',
        'выиграл в МП PaintBall',
        'вышел из-за стола в DICE',
        'выиграл в DICE',
        'сделал ставку на аункционе (биз)',
        'выиграл в донат рулетку',
        'обмен транспорта',
        'сменил ник',
        'поиск транспорта',
        'использовал аптечку в бизнесе',
        'выдал деньги игроку',
        'купил подвал',
        'купил подвал у',
        'пополнил налог бизнеса',
        'пополнил бизнес',
        'снял с бизнеса',
        'купил улучшение для бизнеса',
        'перевел на организацию',
        'приобрел что-то в аптеке',
        'приобрел что-то в магазине',
        'приобрел что-то в баре',
        'сдача на права',
        'перекраска авто',
        'покупка тюнинга на авто',
        'покупка одежды в магазине',
        'отбуксировал транспорт',
        'продал транспорт в госс',
        'поиск бизнеса',
        'улучшение подвала',
        'пополнил склад подвала',
        'снял со склада подвала',
        'сдал дом в аренду',
        'купил улучшения для дома',
        'положил в домашний сейф',
        'снял с домашнего сейфа',
        'положил в семейный сейф',
        'снял с семейного сейфа',
        'выставил транспорт на авторынке',
        'покупка БУ транспорта',
        'продажа БУ транспорта',
        'оптала налогов',
        'пополнение телефона',
        'продал ганг зону',
        'продал оружие',
        'продал наркотики',
        'пополнил общак семьи',
        'снял с общака семьи',
        'покупка семян у наркодиллера',
        'закупка товаров в бизнес',
        'услуги адвоката',
        'покупка лицензии на оружие',
        'покупка лицензии на оружие',
        'выплатил премию',
        'получил премию',
        'покупка симкарты',
        'сменил название семьи',
        'создал семью',
        'продал семейную квартиру',
        'штрафстоянка',
        'вход в бизнес',
        'регистрация на МП',
        'купил набор в донате',
        'купил VIP',
        'конвертировал донат',
        'заправка автомобиля',
        'покупка канистры',
        'купил биз под контроль',
        'взял машину на тест драйв',
        'аренда лавки',
        'купил семейную квартиру',
        'поставил ставку на контейнер',
        'продал все с контейнера',
        'продал предмет с контейнера',
        'победа в дуэле',
        'компенсация ЗП',
        'работа развозчиком материалов',
        'победа на гонках',
        'реферальные деньги',
        'промокод',
        'продал подвал',
        'продал дом',
        'работа дальнобойщиком',
        'зарплата развозчиком пиццы',
        'ставка на кости',
        'возврат денег',
        'купил предмет',
        'за промокод',
        'оплата штрафа',
        'прошел квест',
        'прошел спуск на санях',
        'выиграл лотерею',
        'купил лотерейный билет',
        'выиграл кс',
        'купил лицензии в мэрии',
        'продал рыбу'
      ]
    }
  }
}
</script>



// WEBPACK FOOTER //
// LogsTemplate.vue