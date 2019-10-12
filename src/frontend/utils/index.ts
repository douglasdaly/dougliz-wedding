// utils/index.ts
import { Anchor, Link } from '~/types'

/**
 * Converts the given anchor objects to link objects.
 * @param anchors Anchors to convert to link objects.
 * @returns The link objects.
 */
export function anchorsToLinks (anchors: Anchor[]): Link[] {
  return anchors.map( (element: Anchor) => {
    return {
      name: element.name,
      url: element.anchor
    }
  })
}
