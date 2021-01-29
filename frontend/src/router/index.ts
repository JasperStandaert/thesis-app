import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Patient from '../views/Patient.vue';
import Search from '../views/Search.vue';
import AddPatient from '../views/AddPatient.vue';

Vue.use(VueRouter);

const routes: RouteConfig[] = [
  {
    path: '/',
    name: '/main',
    component: () => import(/* webpackChunkName: "about" */ '../views/Patients.vue'),
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
  {
    path: '/add_patient',
    name: 'Add',
    component: AddPatient,
  },
];

const router = new VueRouter({
  routes,
  mode: 'history',
});

export default router;
