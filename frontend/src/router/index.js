import { createRouter, createWebHistory } from "vue-router"
import Home from "../views/Home.vue"

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/statistics",
    name: "Statistics",
    component: () => import("../views/Statistics.vue")
  },
  {
    path: "/devices",
    name: "Devices",
    component: () => import("../views/Devices.vue")
  },
  {
    path: '/:pathMatch(.*)*',
    component: () => import("../views/PageNotFound.vue")
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
