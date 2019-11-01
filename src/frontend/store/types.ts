// store/types.ts
import { ActionContext } from 'vuex'

import { Link, User } from '~/types'

export interface RootState {
  // Permissions
  isAllowed: boolean,

  // User
  user: User | null,

  // Display
  mainLinks: Link[],
  pageLinks: Link[],
}

export interface RootActionContext extends ActionContext<RootState, RootState> {}
