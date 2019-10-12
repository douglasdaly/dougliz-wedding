// store/wedding/types.ts
import { Event, Person } from '~/types'

export interface WeddingState {
  bride: Person,
  groom: Person,
  ceremony: Event
}
