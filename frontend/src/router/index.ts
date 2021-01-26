import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Patients from '../views/Patients.vue';
import Patient from '../views/Patient.vue';
import Search from '../views/Search.vue';

Vue.use(VueRouter);

const routes: RouteConfig[] = [
  {
    path: '/',
    name: '/main',
    component: () => import(/* webpackChunkName: "about" */ '../views/Patients.vue')
  },
  {
    path: '/search',
    name: 'Search',
    component: Search,
  },
  {
    path: '/patient',
    name: 'Patient',
    component: Patient,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
