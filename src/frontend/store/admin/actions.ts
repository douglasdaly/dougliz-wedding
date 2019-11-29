// store/wedding/actions.ts
import { ActionContext, ActionTree } from 'vuex'
import { mdiClipboardAccountOutline } from '@mdi/js'

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
          { name: 'Events', url: 'wedding/events', icon: 'mdi-calendar-heart' },
          { name: 'Guests', url: 'wedding/guests', icon: mdiClipboardAccountOutline },
        ]
      }
      commit('ADD_TOOL_GROUP', weddingTools)
    }
  },
  superUserToolsInit({ commit }: AdminActionContext, payload: User) {
    if (payload.isSuperuser) {
      const stTitle = {
        name: 'System Tools',
      };
      commit('ADD_TOOL_GROUP', stTitle);

      const stUsers = {
        main: { name: 'Users', url: 'config/users', icon: 'mdi-account-group' },
        links: [
          { name: 'View Users', url: 'config/users', icon: 'mdi-menu' },
          { name: 'Create User', url: 'config/users/create', icon: 'mdi-plus' },
        ],
      };
      commit('ADD_TOOL_GROUP', stUsers);

      const stPermissions = {
        main: { name: 'Permissions', url: 'config/permissions', icon: 'mdi-account-lock-outline' },
        links: [],
      };
      commit('ADD_TOOL_GROUP', stPermissions);

      const stSettings = {
        links: [
          { name: 'Settings', url: 'config/settings', icon: 'mdi-settings-outline' },
        ],
      };
      commit('ADD_TOOL_GROUP', stSettings);
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
