import request from '@/utils/request'

export function order(data) {
  return request({
    //'/vue-admin-template/user/login',
    // url: '/admin/acl/index/login',
    url: 'order/list',
    method: 'post',
    data
  })
}

export function size(params) {
  return request({
    //'/vue-admin-template/user/login',
    // url: '/admin/acl/index/login',
    url: 'size/list',
    method: 'get',
    params
  })
}









