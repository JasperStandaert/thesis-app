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
import VoerroTagsInput from '@voerro/vue-tagsinput';
import { Network } from "vue-vis-network";
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue';
import 'material-design-icons-iconfont/dist/material-design-icons.css'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.component('network', Network)
Vue.use(VueMaterial);
Vue.component('tags-input', VoerroTagsInput);
Vue.use(Vuetify);
Vue.use(Vuesax);
Vue.config.productionTip = false;



new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
