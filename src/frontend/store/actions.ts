// store/wedding/actions.ts
import { ActionTree } from 'vuex'

import { RootActionContext, RootState } from './types'
import { Link } from '~/types'

import { removeLocalToken } from '~/utils/tokens'

export const actions: ActionTree<RootState, RootState> = {

  async nuxtServerInit ({ dispatch }: RootActionContext) {
    await Promise.all([
      // - Root actions
      dispatch('fetchDisplaySettings'),
      // - Modules
      dispatch('wedding/nuxtServerInit')
    ])
  },

  // Permissions
  setAllowed({ commit }: RootActionContext, payload: boolean) {
    commit('SET_ALLOWED', payload)
  },

  // User
  async userLogin ({ commit, dispatch }: RootActionContext, payload: { username: string, password: string }) {
    const user = await this.$api.userLogin(payload.username, payload.password)
    if (user) {
      dispatch('setAllowed', true)
      commit('SET_USER', user)
      return true
    }
    return false
  },

  async autoLogin ({ commit, dispatch }: RootActionContext, payload?: string) {
    const user = await this.$api.tokenLogin(payload)
    if (user) {
      dispatch('setAllowed', true)
      commit('SET_USER', user)
      return true
    }
    return false
  },

  userLogout ({ commit, dispatch }: RootActionContext) {
    dispatch('setAllowed', false)
    commit('CLEAR_USER')
    removeLocalToken()
  },

  // Display
  setMainLinks ({ commit }: RootActionContext, payload?: Link[]) {
    if (!payload) {
      payload = []
    }
    commit('UPDATE_MAIN_LINKS', payload)
  },

  setPageLinks ({ commit }: RootActionContext, payload?: Link[]) {
    if (!payload) {
      payload = []
    }
    commit('UPDATE_PAGE_LINKS', payload)
  },

  clearAllLinks ({ dispatch }: RootActionContext) {
    dispatch('setMainLinks')
    dispatch('setPageLinks')
  },
}

export default actions
