// types/index.ts
export interface Name {
  title?: string,
  first: string,
  middle?: string,
  last: string,
  suffix?: string,
  short?: string
}

export interface Address {
  name?: string,
  line1: string,
  line2?: string,
  line3?: string,
  city: string,
  state?: string,
  zipCode?: number,
  country?: string
}

export interface ContactInfo {
  name?: string,
  phone?: string,
  mobile?: string,
  email: string,
  otherType?: string,
  otherValue?: string,
  preferredMethod: string
}

export interface Person {
  name: Name,
  contact: ContactInfo,
  address?: Address
}

export interface Event {
  name: string,
  date: Date,
  start?: Date,
  end?: Date,
  address?: Address
}

export interface Anchor {
  name: string,
  anchor: string
}

export interface Link {
  external?: boolean,
  name: string,
  url: string,
  newPage?: boolean
}
