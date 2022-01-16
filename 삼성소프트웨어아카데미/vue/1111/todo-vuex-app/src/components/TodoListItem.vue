<template>
  <div>
    <div>
      <span
        @click="updateTodoStatus"
        :class="{ 'is-completed': todo.isCompleted }"
      >
      {{ todo.title }}
      </span>
      <button @click="deleteTodo">Delete</button>
    </div>

  </div>
</template>

<script>
// import { mapActions } from 'vuex'

export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object
    }
  },
  methods: {
    deleteTodo: function () {
      this.$store.dispatch('deleteTodo', this.todo)
    },
    updateTodoStatus: function () {
      this.$store.dispatch('updateTodoStatus', this.todo)
    }
    // ...mapActions([
    //   'deleteTodo',
    //   'updateTodoStatus'
    // ])
  }
}
</script>

<style>
.is-completed {
  text-decoration: line-through;
  color: red;
}
</style>