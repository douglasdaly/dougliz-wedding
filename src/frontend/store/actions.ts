// store/wedding/actions.ts
import { ActionTree } from 'vuex'

import { RootActionContext, RootState } from './types'
import { getAllowed } from '~/api/guest-auth'

export const actions: ActionTree<RootState, RootState> = {
  async nuxtServerInit ({ dispatch }: RootActionContext) {
    await Promise.all([
      // - Root actions
      dispatch('fetchAllowed'),
      // - Modules
      dispatch('wedding/nuxtServerInit')
    ])
  },

  // Basic allowed perms
  async fetchAllowed ({ commit }: RootActionContext) {
    const data = await getAllowed()
    commit('UPDATE_ALLOWED', data)
  },
  setAllowed({ commit }: RootActionContext, payload) {
    commit('UPDATE_ALLOWED', payload)
  }
}

export default actions
