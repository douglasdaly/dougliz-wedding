// store/wedding/getters.ts
import { GetterTree } from 'vuex'

import { RootState } from '../types'
import { WeddingState } from './types'

import { IName } from '~/types'

export const getters: GetterTree<WeddingState, RootState> = {
  brideName (state: WeddingState): IName {
    return state.bride.name
  },
  groomName (state: WeddingState): IName {
    return state.groom.name
  }
}

export default getters
