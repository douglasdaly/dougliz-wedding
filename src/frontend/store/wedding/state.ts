// store/wedding/state.ts
import { WeddingState } from './types'

export const state = (): WeddingState => ({
  bride: {
    name: {
      first: 'The',
      last: 'Bride'
    },
    contact: {
      email: 'thebride@example.com',
      preferredMethod: 'email'
    }
  },
  groom: {
    name: {
      first: 'The',
      last: 'Groom'
    },
    contact: {
      email: 'thegroom@example.com',
      preferredMethod: 'email'
    }
  },
  wedding: {
    name: 'Ceremony',
    date: new Date('2020-09-26T15:00:00')
  }
})

export default state
