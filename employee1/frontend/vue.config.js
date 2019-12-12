// module.exports = {
//     assetsDir: 'static',
// };
proxy: {
        "/api":{
          target:"http://127.0.0.1:8000/",
          changeOrigin: true  // 是否代理
        }
    };//设置代理,
