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
    date: new Date('2020-09-26T15:00:00'),
    address: {
      name: "St. Saintly's Church",
      line1: "42 All Saints Blvd.",
      city: "Anytown",
      state: "PA",
      zipCode: 99999,
      country: "United States"
    }
  },
  settings: {
    guestInfoRedirect: true,
  }
})

export default state
