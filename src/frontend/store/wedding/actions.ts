// store/wedding/actions.ts
import { ActionContext, ActionTree } from 'vuex'

import { RootState } from '../types'
import { WeddingState } from './types'

import { getBride, getGroom } from '~/api/wedding'

interface WeddingActionContext extends ActionContext<WeddingState, RootState> {}

export const actions: ActionTree<WeddingState, RootState> = {
  nuxtServerInit ({ dispatch }: WeddingActionContext) {
    dispatch('fetchData')
  },
  fetchData ({ dispatch }: WeddingActionContext) {
    dispatch('fetchBride')
    dispatch('fetchGroom')
  },
  async fetchBride ({ commit }: WeddingActionContext) {
    const brideData = await getBride()
    commit('UPDATE_BRIDE', brideData)
  },
  async fetchGroom ({ commit }: WeddingActionContext) {
    const groomData = await getGroom()
    commit('UPDATE_GROOM', groomData)
  }
}

export default actions
