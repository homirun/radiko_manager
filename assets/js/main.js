import modal from './modal.vue'
import timeTable from './timeTable.vue'
import Vue from 'vue'
import axios from 'axios'
//import router from 'vue-router'

Vue.config.delimiters =['<%', '%>'];
Vue.component('modal', modal);
Vue.component('time-table', timeTable);

const app = new Vue({
    data:{
        showmodal: false,
    },
}).$mount('#app');