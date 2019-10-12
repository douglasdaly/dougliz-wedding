// store/wedding/mutations.ts
import { MutationTree } from 'vuex'

import { WeddingState } from './types'

import { Person } from '~/types'

export const mutations: MutationTree<WeddingState> = {
  UPDATE_BRIDE (state: WeddingState, payload: Person) {
    state.bride = payload
  },
  UPDATE_GROOM (state: WeddingState, payload: Person) {
    state.groom = payload
  }
}

export default mutations
