
// The Vue build version to load with the `import` command

// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

import Vue from 'vue';

// import router from './router';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import store from './store';
import 'default-passive-events';
import "babel-polyfill";
import axios from "axios";
import XLSX from 'xlsx';
import Axios from 'axios';
import router from './router';
import App from './App';

Vue.prototype.$axios = Axios
let getCookie = function (cookie) {
    let reg = /csrftoken=([\w]+)[;]?/g
    return reg.exec(cookie)[1]
}
Axios.interceptors.request.use(
  function(config) {
    // 在post请求前统一添加X-CSRFToken的header信息
    let cookie = document.cookie;
    if(cookie && config.method == 'post'){
      config.headers['X-CSRFToken'] = getCookie(cookie);
    }
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);


 

//自己写的样式

// import './style/theme.css'

// import './style/characters.css'

 

// 注册element-ui

Vue.use(ElementUI)

Vue.prototype.$axios = axios
 

Vue.config.productionTip = false



/* eslint-disable no-new */

new Vue({

  el: '#app',

  router,
  // store,

  components: { App },

  template: '<App/>'

})
