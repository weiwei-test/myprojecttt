module.exports = {
  publicPath: process.env.NODE_ENV === "production" ? "/vueDataV/" : "/",
  productionSourceMap: false,
  lintOnSave: false,
  devServer: {
    port: 8081,
    proxy: {
      //代理跨域
      '': {
        // target: 'http://39.98.123.211:8170', //获取登录用户信息
        target: 'http://127.0.0.1:8000', //获取登录用户信息
        changOrigin: true,
        pathRewrite: { '^': '' }
      }
    }
    // proxy: {
    //   "/api": {
    //     target: "https://api.github.com",
    //     changeOrigin: true,
    //     ws: false,
    //     pathRewrite: {
    //       "^/api": ""
    //     }
    //   }
    // }
  },
  configureWebpack: {
    // 把原本需要写在webpack.config.js中的配置代码 写在这里 会自动合并
    externals: {
      'jquery': '$',
      'echarts': 'echarts',
      'axios': 'axios'
    }
  }
};