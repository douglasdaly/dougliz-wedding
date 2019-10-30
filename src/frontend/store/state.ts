// store/state.ts
import { RootState } from './types'

export const state = (): RootState => ({
  isAllowed: false,
  mainLinks: [],
  pageLinks: [],
})

export default state
