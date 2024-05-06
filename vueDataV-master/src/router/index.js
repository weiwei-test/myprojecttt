import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)
import Layout from '@/layout'


const routes = [
  {
    path: '/',
    name: 'Login',
    component: () => import('@/views/Login.vue'),
    meta: {
      title: '登录界面'
    }
  },
  {
    path: '/login',
    redirect: '/'
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import('@/views/Home.vue'),
    meta: {
      title: '酷屏首页统计图'
    }
  },
  {
    path: '/brand',
    name: 'Brand',
    component: () => import('@/views/Brand.vue'),
    meta: {
      title: '大屏主页'
    }
  },
  {
    path: '/dmsorder',
    name: 'Dmsorder',
    component: () => import('@/views/Dmsorder.vue'),
    meta: {
      title: 'dms下单'
    }
  },
  {
    path: '/mesacpt',
    name: 'Mesacpt',
    component: () => import('@/views/Mesacpt.vue'),
    meta: {
      title: 'mes接单'
    }
  }
  
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
