import Vue from "vue";
import VueRouter from "vue-router";
import Category from "../views/Category";
import Goods from "../views/Goods";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Category",
    component: Category
  },
  {
    path: "/gd",
    name: "Goods",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Goods
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
