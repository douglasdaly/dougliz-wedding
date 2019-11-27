// types/index.ts

// Sub-modules
export * from './config'
export * from './models'

// Basic data structures
export type Dict<T> = { [key: string]: T }

// Links
export interface Anchor {
  name: string,
  anchor: string
}

export interface Link {
  external?: boolean,
  icon?: string,
  name: string,
  url: string,
  newPage?: boolean
}

export interface LinkGroup {
  name?: string,
  main?: Link,
  links?: Link[]
}
