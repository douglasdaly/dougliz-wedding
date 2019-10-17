// utils/display.ts
import { Name, Address } from '~/types'

/**
 * Gets the full name from the given name object.
 * @param name The name object/dictionary to use.
 * @param prefix Whether or not to prepend the prefix.
 * @returns The full name string to use.
 */
export function getFullName(name: Name, includeTitle = false): string {
  const rv = [];
  if (name.title && includeTitle) {
    rv.push(name.title);
  }
  rv.push(name.first);
  if (name.middle) {
    rv.push(name.middle);
  }
  rv.push(name.last);
  if (name.suffix) {
    rv.push(name.suffix);
  }
  return rv.join(' ');
}

/**
 * Gets the short name from the given name object.
 * @param name The name object to get the short name from.
 * @param includeLast Whether to include the last name.
 * @returns The short name string to use.
 */
export function getShortName(name: Name, includeLast = false): string {
  let rv = name.short ? name.short : name.first
  if (includeLast) {
    rv += ` ${name.last}`
  }
  return rv
}

/**
 * Gets a display string for the given date.
 * @param date The date to get the display string for.
 * @param full Whether or not to get the full, formal string.
 * @return The display string to use.
 */
export function getDisplayDate(date: Date, full = false): string {
  let options = {}
  if (full) {
    options = { dateStyle: 'full' }
  } else {
    options = {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    }
  }
  return date.toLocaleDateString("en-US", options)
}

/**
 * Gets a display-friendly string of the given time.
 * @param date The date with the time to display.
 * @param showMinutes Whether or not to show the minutes.
 * @param showType Whether or not to show AM/PM.
 * @returns The display time string to use.
 */
export function getDisplayTime(
  date: Date,
  showMinutes = false,
  showType = true
): string {
  let tHour = date.getHours()
  let tType = 'AM'
  if (tHour >= 12) {
    tType = 'PM'
    if (tHour > 12) {
      tHour -= 12
    }
  }
  let rv = `${tHour}`
  if (showMinutes) {
    rv += `:${date.getMinutes()}`
  }
  if (showType) {
    rv += `${showMinutes ? ' ' : ''}${tType}`
  }
  return rv
}

/**
 * Gets the display lines for the given address.
 * @param address The address object dictionary to use.
 * @returns An array of the address line strings to use.
 */
export function getDisplayAddressLines(
  address: Address,
  includeName = true
): string[] {
  const rv = []
  if (includeName && address.name) {
    rv.push(address.name)
  }
  rv.push(address.line1)
  if (address.line2) {
    rv.push(address.line2)
  }
  if (address.line3) {
    rv.push(address.line3)
  }
  if (address.city && address.state) {
    let tmpStr = `${address.city}, ${address.state}`
    if (address.zipCode) {
      tmpStr += ` ${address.zipCode}`
    }
    rv.push(tmpStr)
  }
  return rv
}
