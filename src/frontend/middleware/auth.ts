// middleware/admin-auth.ts
import { Context, Middleware } from '@nuxt/types'

const authMiddleware: Middleware = ({ redirect, route, store }: Context) => {
  if (!store.getters.isLoggedIn) {
    const rte = { name: 'login', query: {} }
    if (route.name !== "index") {
      rte.query = { next: route.name }
    }
    redirect(rte)
  }
}

export default authMiddleware
