// types/models.ts

// Abstract models
export interface Identified {
  id?: string
}

// Basic models
export interface Name extends Identified {
  title?: string,
  first: string,
  middle?: string,
  last: string,
  suffix?: string,
  short?: string
}

export interface Address extends Identified {
  name?: string,
  line1: string,
  line2?: string,
  line3?: string,
  city: string,
  state?: string,
  zipCode?: number,
  country?: string
}

export interface ContactInfo extends Identified {
  name?: string,
  phone?: string,
  mobile?: string,
  email: string,
  otherType?: string,
  otherValue?: string,
  preferredMethod: string
}

export interface Person extends Identified {
  name: Name,
  contact: ContactInfo,
  address?: Address
}

export interface Event extends Identified {
  name: string,
  date: Date,
  start?: Date,
  end?: Date,
  address?: Address
}

export interface User extends Identified {
  person?: Person,
  email: string,
  isActive: boolean,
  isPoweruser: boolean,
  isSuperuser: boolean,
}
