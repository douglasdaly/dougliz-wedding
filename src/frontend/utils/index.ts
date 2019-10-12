// utils/index.ts
import { IAnchor, ILink } from '~/types'

/**
 * Converts the given anchor objects to link objects.
 * @param anchors Anchors to convert to link objects.
 * @returns The link objects.
 */
export function anchorsToLinks (anchors: IAnchor[]): ILink[] {
  return anchors.map( (element: IAnchor) => {
    return {
      name: element.name,
      url: element.anchor
    }
  })
}
