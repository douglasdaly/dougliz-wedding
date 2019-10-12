// middleware/passcode.ts
import { Middleware } from '@nuxt/types'

const guestAuthMiddleware: Middleware = ({ store, redirect }) => {
  if (!store.state.isAllowed) {
    redirect('/guest-login')
  }
}

export default guestAuthMiddleware
