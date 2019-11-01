// store/state.ts
import { RootState } from './types'

export const state = (): RootState => ({
  // Permissions
  isAllowed: false,

  // Users
  user: null,

  // UI
  mainLinks: [],
  pageLinks: [],
})

export default state
