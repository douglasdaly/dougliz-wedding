// middleware/guest-auth.ts
import { Middleware } from '@nuxt/types'

const guestAuthMiddleware: Middleware = ({ store, redirect, route }) => {
  if (!store.state.isAllowed) {
    const rte = { name: 'guest-login', query: {} }
    if (route.name !== "index") {
      rte.query = { next: route.name }
    }
    redirect(rte)
  }
}

export default guestAuthMiddleware
