/*
* GET /admin/product/baseTrademark/findBaseTrademarkByKeyword/{keyword}
findBaseTrademarkByKeyword

GET /admin/product/baseTrademark/get/{id}
获取BaseTrademark

GET /admin/product/baseTrademark/getTrademarkList
getTrademarkList

POST /admin/product/baseTrademark/inner/findBaseTrademarkByTrademarkIdList
findBaseTrademarkByTrademarkIdList
*
* */

/*获取品牌分页列表数据
* GET /admin/product/baseTrademark/{page}/{limit}
* page:第几页， limit每页显示条数
* */
import request from "@/utils/requestSku"
/*
export function getInfo(token) {
  // token='eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSSkzJzcxT0lFKrShQsjI0MzQzMTK1NDGvBQApMebnIAAAAA.UG2Qj7F7ASMLBugNG67-wKs0Un6ORrneMkSdio0rKhX0o-fd6BC24T1gCzfVVtsNERPzs4Sjwz8JOyPfLazUSA'
  return request({
    //'/vue-admin-template/user/info',
    url: '/admin/acl/index/info',
    method: 'get',
    params: {token}
  })
}*/
export const reqGetTrademark = (page, limit) => {
  return request({
    //  url: '/admin/acl/index/info',
    url: `/admin/product/baseTrademark/${page}/${limit}`,
    method: 'get'
  })

}

/*修改或者添加：
* PUT /admin/product/baseTrademark/update  修改
* POST /admin/product/baseTrademark/save 添加品牌
* */

export const reqAddOrUpdate = (data) => {
  if (data.id) {
    //修改
    return request({
      url: '/admin/product/baseTrademark/update',
      data: data,
      method: 'put'
    })
  } else {
    //添加
    return request({
      url: '/admin/product/baseTrademark/save',
      method: 'post',
      data: data
    })
  }
}

/*DELETE /admin/product/baseTrademark/remove/{id}
删除品牌BaseTrademark
export: 模块中导出函数、对象或原始值，以便在其他文件中可以使用，
export default:默认导出，一个js只能有一个
export const :命名导出，可以有多个，引入用import{}
 */

export const reqTradeDel = (tradeId) => {
  return request({
    url: `/admin/product/baseTrademark/remove/${tradeId}`,
    method: 'delete'
  })
}
