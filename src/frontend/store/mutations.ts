// store/mutations.ts
import { MutationTree } from 'vuex'

import { RootState } from './types'

import { Link } from '~/types'

export const mutations: MutationTree<RootState> = {
  UPDATE_ALLOWED (state: RootState, payload: boolean) {
    state.isAllowed = payload
  },
  UPDATE_MAIN_LINKS (state: RootState, payload?: Link[] | undefined) {
    state.mainLinks = payload
  },
  UPDATE_PAGE_LINKS (state: RootState, payload?: Link[] | undefined) {
    state.pageLinks = payload
  },
}

export default mutations
