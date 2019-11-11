// store/wedding/actions.ts
import { ActionContext, ActionTree } from 'vuex'

import { RootState } from '../types'
import { AdminState } from './types'

import { Link, User } from '~/types'

interface AdminActionContext extends ActionContext<AdminState, RootState> {}

export const actions: ActionTree<AdminState, RootState> = {

  // Setup
  adminInit ({ dispatch, rootGetters }: AdminActionContext) {
    dispatch('clearCrumbs')
    dispatch('adminToolsInit', rootGetters.user)
  },

  // Tools
  adminToolsInit ({ commit, dispatch, rootGetters }: AdminActionContext, payload: User) {
    commit('CLEAR_TOOLS')
    if (rootGetters.isAdmin) {
      const defaultTools = {
        links: [
          { name: 'My Account', url: 'me', icon: 'mdi-account-circle' },
        ],
      }
      commit('ADD_TOOL_GROUP', defaultTools)

      // - Additional user types/tools
      dispatch('powerUserToolsInit', payload)
      dispatch('superUserToolsInit', payload)
    }
  },
  powerUserToolsInit({ commit }: AdminActionContext, payload: User) {
    if (payload.isPoweruser) {
      const weddingTools = {
        name: 'Tools',
        main: { name: 'Wedding', url: 'wedding', icon: 'mdi-cards-heart' },
        links: [
          { name: 'Guests', url: 'wedding/guests', icon: 'mdi-clipboard-account-outline' },
          { name: 'Events', url: 'wedding/events', icon: 'mdi-calendar-heart' },
        ]
      }
      commit('ADD_TOOL_GROUP', weddingTools)
    }
  },
  superUserToolsInit({ commit }: AdminActionContext, payload: User) {
    if (payload.isSuperuser) {
      const superTools = {
        name: 'System Tools',
        links: [
          { name: 'Users', url: 'config/users', icon: 'mdi-account-group' },
          { name: 'Permissions', url: 'config/permissions', icon: 'mdi-account-lock-outline' },
          { name: 'Settings', url: 'config/settings', icon: 'mdi-settings-outline' },
        ],
      }
      commit('ADD_TOOL_GROUP', superTools)
    }
  },

  // Crumbs
  clearCrumbs({ commit }: AdminActionContext) {
    commit('CLEAR_CRUMBS')
  },
  setCrumbs({ commit }: AdminActionContext, payload: Link[]) {
    commit('SET_CRUMBS', payload)
  },
  addCrumb({ commit }: AdminActionContext, payload: Link) {
    commit('ADD_CRUMB', payload)
  },
  removeCrumb({ commit }: AdminActionContext, payload?: Number) {
    if (!payload) {
      payload = 1
    }
    for (let i=0; i < payload; i++) {
      commit('REMOVE_CRUMB')
    }
  },
}

export default actions
