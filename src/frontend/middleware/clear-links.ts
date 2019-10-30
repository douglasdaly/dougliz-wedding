// middleware/passcode.ts
import { Middleware } from '@nuxt/types'

const clearLinksMiddleware: Middleware = ({ store }) => {
  store.dispatch('clearAllLinks')
}

export default clearLinksMiddleware
