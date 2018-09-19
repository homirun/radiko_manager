import Vue from 'vue'

import modal from './modal.vue'
import timeTable from './timeTable.vue'
import VueRouter from 'vue-router'
import routers from './routers.js'

Vue.use(VueRouter);

Vue.config.delimiters =['<%', '%>'];
Vue.component('modal', modal);
Vue.component('time-table', timeTable);

const router  = new VueRouter({
    routes: routers,
    mode: 'history'
});

const app = new Vue({
    router,
    data:{
        showmodal: false,
    },
}).$mount('#app');