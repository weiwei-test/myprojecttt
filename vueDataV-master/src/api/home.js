import request from "@/utils/mockRequest"

export const reqHomeList = () => {
  return request({
    url: '/home/list',
    method: 'get',
  })
}
