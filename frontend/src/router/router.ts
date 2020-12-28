import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import PatientOverview from '../views/PatientOverview.vue'
import Search from '../view/Search.vue'
import PatientPage from '../view/PatientPage.vue'

Vue.use(VueRouter)
const routes: Array<RouteConfig> = [
    {
        path: '/main',
        name: 'Main',
        component: () => import(/* webpackChunkName: "about" */ '../views/Main.vue')
    },
    {
        path: '/patients',
        name: 'PatientOverview',
        component: PatientOverview

    },
    {
        path: '/search',
        name: 'Search',
        component: Search
    },
    {
        path: '/patient',
        name: 'Patient',
        component: PatientPage
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})
