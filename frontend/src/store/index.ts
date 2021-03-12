import Vue from 'vue';
import Vuex, { Store } from 'vuex';
import CreatePersistedState from 'vuex-persistedstate'

Vue.use(Vuex);

const datastate = CreatePersistedState({
  paths: ['patient']
})

export default new Vuex.Store({
  state: {
    patient: {
      first_name: '',
      last_name: '',
      age: '',
      gender: '',
      medication: [],
    },
    interactions: [],
    activeNode: '',
    activeInteraction: [],
  },
  mutations: {
    addInteractions(state, interactions) {
      state.interactions = interactions;
    },
    addMedication(state, meds){
      state.patient.medication = meds
    },
    addPatient(state, patient){
      state.patient = patient
    },
    setActiveInteraction(state, interaction){
      state.activeInteraction = interaction
    },
    setActiveNode(state, node){
      state.activeNode = node
    }
  },
  getters: {
    patient: state => state.patient,
    medication: (state) => state.patient.medication,
    interactions: (state) => state.interactions,
    activeNode: (state) => state.activeNode,
    activeInteraction: (state) => state.activeInteraction,
  },
  plugins: [datastate],
});
