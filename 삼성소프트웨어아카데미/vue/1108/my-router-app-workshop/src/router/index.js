import Vue from 'vue'
import VueRouter from 'vue-router'
import TheLotto from '../views/TheLotto.vue'
import TheLunch from '../views/TheLunch.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: 'lunch',
    name: 'TheLunch',
    component: TheLunch,
  },
  {
    path: '/lotto',
    name: 'TheLotto',
    component: TheLotto
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
