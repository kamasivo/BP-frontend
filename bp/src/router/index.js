import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

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
    path: "/vulnerabilities",
    name: "Vulnerabilities",
    component: () => import("../views/Vulnerabilities.vue")
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
