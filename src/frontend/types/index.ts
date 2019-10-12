// types/index.ts
export interface IName {
  prefix?: string,
  first: string,
  middle?: string,
  last: string,
  suffix?: string,
  short?: string
}

export interface IAddress {
  name?: string,
  line1: string,
  line2?: string,
  line3?: string,
  city: string,
  state?: string,
  zip?: number,
  country?: string
}

export interface IPerson {
  name: IName,
  address?: IAddress
}

export interface IEvent {
  name: string,
  address?: IAddress,
  start: Date,
  end?: Date
}

export interface IAnchor {
  name: string,
  anchor: string
}

export interface ILink {
  external?: boolean,
  name: string,
  url: string,
  newPage?: boolean
}
