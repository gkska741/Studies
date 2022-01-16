<template>
  <div>
    <h1>로또 번호 추천</h1>
    <h2>{{ $route.params.LottoNum}} 개의 번호 추첨</h2>
    <button @click="getLuckyNums">로또를 뽑아보자</button>
    <p> {{ selectedLuckyNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',

  data: function() {
    return {
      selectedLuckyNums: [],
    }
  },
  methods: {
    getLuckyNums: function () {
      const numbers = _.range(1, 46)
      this.selectedLuckyNums = _.sampleSize(numbers, this.$route.params.LottoNum)
    }
  }
}
</script>