// store/wedding/types.ts
import { IEvent, IPerson } from '~/types'

export interface WeddingState {
  bride: IPerson,
  groom: IPerson,
  ceremony: IEvent
}
