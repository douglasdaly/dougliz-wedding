// store/mutations.ts
import { MutationTree } from 'vuex'

import { RootState } from './types'

export const mutations: MutationTree<RootState> = {
  UPDATE_ALLOWED (state: RootState, payload: boolean) {
    state.isAllowed = payload
  }
}

export default mutations
