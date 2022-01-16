<template>
  <div>
    <h1>점심 메뉴</h1>
    <button @click="getLunchMenu">메뉴를 뽑아보자</button>
    <p>{{ selectedLunchMenu }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'TheLunch',

  data: function() {
    return {
      lunchMenus: ['치킨', '피자', '떡볶이'],
      selectedLunchMenu: [],
    }
  },
  methods: {
    getLunchMenu: function () {
      const menus = this.lunchMenus
      this.selectedLunchMenu = _.sampleSize(menus, 1)
    }
  }
}
</script>
