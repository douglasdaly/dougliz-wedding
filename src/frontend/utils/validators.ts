// validators.ts

/**
 * Checks the given string to determine if it's a valid zip code.
 * @param value The zip code input value to validate.
 */
export function validZip (value: string | undefined): boolean {
  if (!value) {
    return false
  }
  const re = /^\d{5}(-?\d{4})?$/
  return re.test(value)
}

/**
 * Checks the given string to determine if it's a valid phone number.
 * @param value The phone number input value to validate.
 */
export function validPhone(value: string | undefined): boolean {
  if (!value) {
    return false
  }
  const re = /^[+]?[(]?[0-9]{3}[)]?[-\s.]?[0-9]{3}[-\s.]?[0-9]{4,6}$/i
  return re.test(value)
}
