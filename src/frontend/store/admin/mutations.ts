// store/wedding/mutations.ts
import Vue from 'vue'
import { MutationTree } from 'vuex'

import { AdminState } from './types'
import { Link, LinkGroup } from '~/types'

export const mutations: MutationTree<AdminState> = {
  // Crumbs
  CLEAR_CRUMBS (state: AdminState) {
    Vue.set(state, 'crumbLinks', [])
  },
  SET_CRUMBS (state: AdminState, payload: Link[]) {
    Vue.set(state, 'crumbLinks', payload)
  },
  ADD_CRUMB (state: AdminState, payload: Link) {
    state.crumbLinks.push(payload)
  },
  REMOVE_CRUMB (state: AdminState) {
    if (state.crumbLinks.length > 0) {
      state.crumbLinks.pop()
    }
  },

  // Tools
  CLEAR_TOOLS (state: AdminState) {
    Vue.set(state, 'toolLinks', [])
  },
  ADD_TOOL_GROUP (state: AdminState, payload: LinkGroup) {
    state.toolLinks.push(payload)
  },
}

export default mutations
