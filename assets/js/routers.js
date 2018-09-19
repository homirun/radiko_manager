import timeTable from './timeTable.vue'
import reserveCheck from './reserveCheck.vue'
import test from './test.vue'


export default [
    {
        path: '/',
        component: timeTable,
    },
    {
        path: '/reserveCheck',
        component: reserveCheck,
    },
]