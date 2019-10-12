// store/wedding/state.ts
import { WeddingState } from './types'

export const state = (): WeddingState => ({
  bride: {
    name: {
      first: 'The',
      last: 'Bride'
    }
  },
  groom: {
    name: {
      first: 'The',
      last: 'Groom'
    }
  },
  ceremony: {
    name: 'Ceremony',
    start: new Date('2020-09-26T15:00:00')
  }
})

export default state
