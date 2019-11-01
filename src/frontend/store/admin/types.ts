// store/wedding/types.ts
import { Link } from '~/types'

export interface AdminState {
  toolLinks: Link[],
  crumbLinks: Link[]
}
