// store/wedding/getters.ts
import { GetterTree } from 'vuex'

import { RootState } from './types'
import { User } from '~/types'

import { getShortName } from '~/utils/display'

export const getters: GetterTree<RootState, RootState> = {
  user (state: RootState): User | undefined {
    if (state.user) {
      return state.user
    }
  },

  userDisplayName (state: RootState): string | undefined {
    if (state.user) {
      if (state.user.person) {
        return getShortName(state.user.person.name)
      } else {
        return state.user.email
      }
    }
  },

  userEmail (state: RootState): string | undefined {
    if (state.user) {
      return state.user.email
    }
  },

  isLoggedIn (state: RootState): boolean {
    if (state.user) {
      return true
    }
    return false
  },

  isActive (state: RootState): boolean {
    if (state.user) {
      return state.user.isActive
    }
    return false
  },

  isAdmin (state: RootState): boolean {
    if (state.user) {
      return (
        state.user.isActive
        && (state.user.isPoweruser || state.user.isSuperuser)
      )
    }
    return false
  },
}

export default getters
