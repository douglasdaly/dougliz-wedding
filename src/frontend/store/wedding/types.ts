// store/wedding/types.ts
import { Event, Person } from '~/types'

export interface WeddingSettings {
  guestInfoRedirect: boolean
}

export interface WeddingState {
  bride: Person,
  groom: Person,
  engagementParty?: Event,
  welcome?: Event,
  rehearsalDinner?: Event,
  wedding?: Event,
  reception?: Event,
  brunch?: Event,
  settings: WeddingSettings
}
