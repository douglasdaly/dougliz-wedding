// store/wedding/getters.ts
import { GetterTree } from 'vuex'

import { RootState } from '../types'
import { WeddingState } from './types'

import { Name } from '~/types'

export const getters: GetterTree<WeddingState, RootState> = {
  brideName (state: WeddingState): Name {
    return state.bride.name
  },
  groomName (state: WeddingState): Name {
    return state.groom.name
  },
  weddingDate (state: WeddingState): Date | undefined {
    if (state.wedding) {
      return state.wedding.date
    }
  }
}

export default getters
