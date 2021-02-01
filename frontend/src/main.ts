import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import Vuesax from 'vuesax';
import 'vuesax/dist/vuesax.css';
import VueVega from 'vue-vega';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css';
import VoerroTagsInput from '@voerro/vue-tagsinput';
import Return from './components/Return.vue';
import { Network } from "vue-vis-network";


Vue.component('network', Network)
Vue.component('return', Return)
Vue.use(VueMaterial);
Vue.component('tags-input', VoerroTagsInput);
Vue.use(Vuetify);
Vue.use(Vuesax);
Vue.use(VueVega);
Vue.config.productionTip = false;



new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
