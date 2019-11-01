// store/wedding/actions.ts
import { ActionContext, ActionTree } from 'vuex'

import { RootState } from '../types'
import { AdminState } from './types'

interface AdminActionContext extends ActionContext<AdminState, RootState> {}

export const actions: ActionTree<AdminState, RootState> = {
}

export default actions
