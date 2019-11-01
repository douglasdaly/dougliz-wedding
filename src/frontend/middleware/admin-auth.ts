// middleware/admin-auth.ts
import { Context, Middleware } from '@nuxt/types'

const adminAuthMiddleware: Middleware = ({ redirect, store }: Context) => {
  if (!store.getters.isAdmin) {
    redirect(403, "/", { message: 'Insufficient privileges' })
  }
}

export default adminAuthMiddleware
