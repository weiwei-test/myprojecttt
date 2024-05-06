import request from '@/utils/request'

export function login(data) {
  return request({
    //'/vue-admin-template/user/login',
    // url: '/admin/acl/index/login',
    url: 'user/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  // token='eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSSkzJzcxT0lFKrShQsjI0MzQzMTK1NDGvBQApMebnIAAAAA.UG2Qj7F7ASMLBugNG67-wKs0Un6ORrneMkSdio0rKhX0o-fd6BC24T1gCzfVVtsNERPzs4Sjwz8JOyPfLazUSA'
  return request({
    //'/vue-admin-template/user/info',
    // url: '/admin/acl/index/info',
    url: 'user/detail',
    method: 'get',
    params: {token}
  })
}

export function logout() {
  return request({
    //'/vue-admin-template/user/logout',
    // url: '/admin/acl/index/logout',
    url: 'user/logout',
    method: 'post'
  })
}
