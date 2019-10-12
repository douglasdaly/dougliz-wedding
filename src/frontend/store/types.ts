// store/types.ts
import { ActionContext } from 'vuex'

export interface RootState {
  isAllowed: boolean
}

export interface RootActionContext extends ActionContext<RootState, RootState> {}
