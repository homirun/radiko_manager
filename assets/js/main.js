import modal from './modal.vue'
import Vue from 'vue'
import axios from 'axios'
//import router from 'vue-router'

Vue.config.delimiters =['<%', '%>'];
Vue.component('modal', modal);

console.log("hoge");

const app = new Vue({
    data:{
        showmodal: false,
    },
}).$mount('#app');