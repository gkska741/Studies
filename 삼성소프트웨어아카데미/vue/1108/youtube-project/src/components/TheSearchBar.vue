<template>
  <div>
    <input @keyup.enter="onInputKeyword" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',

  methods: {
    onInputKeyword: function () {
      this.$emit('input-change', event.target.value)
    }
  }
}
</script>

<style>

</style>
