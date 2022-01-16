<template>
  <div id="app">
    <h1>Youtube Project</h1>
    <the-search-bar @input-change="onInputKeyword" />
  </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar.vue'
import axios from 'axios'
const API_KEY = 'AIzaSyBsSq23XPah3bcxxMRPmqH9Lh4O04mjc-k'
const API_URL = ''
export default {
  name: 'App',
  components: {
    TheSearchBar,
  },
  data: function () {
    return {
      searchKeyword: null,
      videos: [],
    }
  },
  methods: {
    onInputKeyword: function (inputKeyword) {
      console.log(inputKeyword)
      this.searchKeyword = inputKeyword

      const params = {
        key: API_KEY,
        part: 'snippet',
        maxResults: 10,
        order: 'date',
        q: this.searchKeyword,
        type: 'video',
      }
      axios({
        method: 'get',
        url: API_URL,
        params,
      })
        .then
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
