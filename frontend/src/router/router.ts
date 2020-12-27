import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Main from '../view/Main.vue'

Vue.use(VueRouter)
const routes: Array<RouteConfig> = [
    {
        path: '/',
        name: 'Main',
        component: () => import(/* webpackChunkName: "about" */ '../views/Main.vue')
    },
]
