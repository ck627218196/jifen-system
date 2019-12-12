import Vue from 'vue'
import Router from 'vue-router'
import login3 from '@/components/login3'
import managermark from '@/components/managermark'
import assess from '@/components/assess'
import assessdata from '@/components/assessdata'
import attence from '@/components/attence'
import download from '@/components/download'
import permission from '@/components/permission'
import managermarkdata from '@/components/managermarkdata'
// import fenye from '@/components/fenye'
// import ceomark from '@/components/ceomark'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login3',
      component: login3
    },
    {
      // path: '/managermark/:id',
      path: '/managermark',
      name: 'managermark',
      component: managermark
    },
    {
      // path: '/managermark/:id',
      path: '/managermark/managermarkdata',
      name: 'managermarkdata',
      component: managermarkdata
    },
    {
      path: '/assess',
      name: 'assess',
      component: assess
    },
    {
      path: '/assess/assessdata',
      name: 'assessdata',
      component: assessdata
    },
    {
      path: '/attence',
      name: 'attence',
      component: attence
    },
    // {
    //   path: '/others',
    //   name: 'others',
    //   component: others
    // },
    {
      // path: '/download',
      path: '/download',
      name: 'download',
      component: download
    },
    {
      path: '/download/permission',
      name: 'permission',
      component: permission
    },
    // {
    //   path: '/fenye',
    //   name: 'fenye',
    //   component: fenye
    // },
    // {
    //   path: '/ceomark',
    //   name: 'ceomark',
    //   component: ceomark
    // }
  ]
})
