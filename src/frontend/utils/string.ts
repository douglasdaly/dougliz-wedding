// utils/string.ts

/**
 * Converts a camel-cased string to be capitalized & spaced
 * @param value The camel-case string to convert to text
 * @returns The capitalized & spaced, converted string
 */
export function camelToString (value: string): string {
  let rv = value.charAt(0).toUpperCase()
  if (value.length > 1) {
    rv = rv + value.substring(1).replace(/[A-Z]|[0-9]+/g, ' $&')
  }
  return rv
}
