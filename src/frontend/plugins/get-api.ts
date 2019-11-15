// plugins/api.ts
import { Plugin } from '@nuxt/types'

import { IAPI } from '~/api/types'
import API from '~/api'

declare module 'vue/types/vue' {
  interface Vue {
    $api: IAPI
  }
}

declare module '@nuxt/types' {
  interface NuxtAppOptions {
    $api: IAPI
  }
}

declare module 'vuex/types/index' {
  interface Store<S> {
    $api: IAPI
  }
}

const apiPlugin: Plugin = (ctx, inject) => {
  const api = API(ctx.$axios)
  inject('api', api)
}

export default apiPlugin
