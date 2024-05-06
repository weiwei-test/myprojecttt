//product统一暴露
import * as trademark from './product/trademark' //* 一次性引入所有export const

import permission from "@/api/acl/permission";
import role from "@/api/acl/role";
import * as user from "@/api/acl/user";
import * as order from "@/api/order";

export default {
  trademark,
  permission,
  role,
  user,
  order
}
