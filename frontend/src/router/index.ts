import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Patient from '../views/Patient.vue';
import Search from '../views/Search.vue';
import AddPatient from '../views/AddPatient.vue';
import AddDrug from '../views/AddDrug.vue'
import GraphView from '../views/GraphView.vue'

Vue.use(VueRouter);

const routes: RouteConfig[] = [
  {
    path: '/',
    name: 'Patients',
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
    path: '/patient/graph',
    name: 'Patient-Graph',
    component: GraphView,
    meta: {transitionName: 'slide'}
  },
  {
    path: '/add_patient',
    name: 'AddPatient',
    component: AddPatient,
  },
  {
    path: '/add_drug',
    name: 'AddDrug',
    component: AddDrug,
  }
];

const router = new VueRouter({
  routes,
  mode: 'history',
});

export default router;
