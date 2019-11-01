// store/mutations.ts
import Vue from 'vue'
import { MutationTree } from 'vuex'

import { RootState } from './types'

import { Link, User } from '~/types'

export const mutations: MutationTree<RootState> = {
  // Permissions
  SET_ALLOWED (state: RootState, payload: boolean) {
    state.isAllowed = payload
  },

  // User
  SET_USER (state: RootState, payload: User) {
    Vue.set(state, 'user', payload)
  },
  CLEAR_USER (state: RootState) {
    Vue.set(state, 'user', null)
  },

  // Display
  UPDATE_MAIN_LINKS (state: RootState, payload?: Link[]) {
    Vue.set(state, 'mainLinks', payload)
  },
  UPDATE_PAGE_LINKS (state: RootState, payload?: Link[]) {
    Vue.set(state, 'pageLinks', payload)
  },
}

export default mutations
