// store/wedding/types.ts
import { Link, LinkGroup } from '~/types'

export interface AdminState {
  toolLinks: LinkGroup[],
  crumbLinks: Link[]
}
