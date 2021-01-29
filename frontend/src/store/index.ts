import Vue from 'vue';
import Vuex, { Store } from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    patientdata: [],
    medication: [],
  },
  mutations: {
    addPatients(state, patientdata) {
      state.patientdata = patientdata;
    },
    addMedication(state, medicationData) {
      state.medication = medicationData;
    },
  },
  getters: {
    patientdata: (state) => state.patientdata,
    medication: (state) => state.medication,
  },
  actions: {
  },
  modules: {
  },
});
