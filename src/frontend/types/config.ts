// types/config.ts

export interface Setting<T> {
  name: string,
  value?: T,
  required: boolean,
}
