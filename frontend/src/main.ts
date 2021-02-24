import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import Vuesax from 'vuesax';
import 'vuesax/dist/vuesax.css';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css';
import { Network } from "vue-vis-network";
import "vis-network/styles/vis-network.css";
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import '@mdi/font/css/materialdesignicons.css'
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css'
import VueVega from 'vue-vega'

import './assets/style/style.scss'

Vue.component('v-select', vSelect)
Vue.component('network', Network)
Vue.use(VueVega)
Vue.use(VueMaterial);
Vue.use(Vuetify);
Vue.use(Vuesax);
Vue.config.productionTip = false;



new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
