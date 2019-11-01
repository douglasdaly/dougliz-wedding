// middleware/admin-auth.ts
import { Context, Middleware } from '@nuxt/types'

const authMiddleware: Middleware = ({ redirect, route, store }: Context) => {
  if (!store.getters.isLoggedIn) {
    let rPath = '/login'
    if (route.name !== "index") {
      rPath += `?next=${route.name}`
    }
    redirect(rPath)
  }
}

export default authMiddleware
