import { createRouter, createWebHistory } from "vue-router";
const Bio = () => import("@/views/Bio.vue");
const Blog = () => import("@/views/Blog.vue");
const Projects = () => import("@/views/Projects.vue");

const routes = [
  {
    path: "/",
    name: "Bio",
    component: Bio,
  },
  {
    path: "/blog",
    name: "Blog",
    component: Blog,
  },
  {
    path: "/projects",
    name: "Projects",
    component: Projects,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
});

export default router;
