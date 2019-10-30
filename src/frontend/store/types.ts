// store/types.ts
import { ActionContext } from 'vuex'

import { Link } from '~/types'

export interface RootState {
  isAllowed: boolean,
  mainLinks?: Link[],
  pageLinks?: Link[],
}

export interface RootActionContext extends ActionContext<RootState, RootState> {}
