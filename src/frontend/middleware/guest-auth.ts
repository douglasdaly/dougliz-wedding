// middleware/guest-auth.ts
import { Middleware } from '@nuxt/types'

const guestAuthMiddleware: Middleware = ({ store, redirect, route }) => {
  if (!store.state.isAllowed) {
    let rPath = '/guest-login'
    if (route.name !== "index") {
      rPath += `?next=${route.name}`
    }
    redirect(rPath)
  }
}

export default guestAuthMiddleware
