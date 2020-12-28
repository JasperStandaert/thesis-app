import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'

Vue.use(VueRouter)
const routes: Array<RouteConfig> = [
    {
        path: '/main',
        name: 'Main',
        component: () => import(/* webpackChunkName: "about" */ '../views/Main.vue')
    },
]

const router = new VueRouter({
    mode: 'history',
    routes
})
