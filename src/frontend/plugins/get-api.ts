// plugins/api.ts
import { Context } from 'vm'

import API from '~/api'

export default (ctx: Context, inject: CallableFunction) => {
  const api = API(ctx.$axios)
  ctx.$api = api
  inject('api', api)
}
