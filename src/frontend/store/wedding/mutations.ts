// store/wedding/mutations.ts
import { MutationTree } from 'vuex'

import { WeddingState } from './types'

import { IPerson } from '~/types'

export const mutations: MutationTree<WeddingState> = {
  UPDATE_BRIDE (state: WeddingState, payload: IPerson) {
    state.bride = payload
  },
  UPDATE_GROOM (state: WeddingState, payload: IPerson) {
    state.groom = payload
  }
}

export default mutations
