// api/wedding.ts
import { IPerson } from '~/types'

const DUMMY_BRIDE: IPerson = {
  name: {
    first: 'Elizabeth',
    middle: 'Devery',
    last: 'Kneuer',
    short: 'Liz'
  }
}

const DUMMY_GROOM: IPerson = {
  name: {
    first: 'Douglas',
    middle: 'James',
    last: 'Daly',
    suffix: 'Jr.',
    short: 'Doug'
  }
}

export const getBride = async (): Promise<IPerson> => {
  const data = await new Promise<IPerson>(resolve =>
    setTimeout(() => resolve(DUMMY_BRIDE), 500)
  )
  return data
}

export const getGroom = async (): Promise<IPerson> => {
  const data = await new Promise<IPerson>(resolve =>
    setTimeout(() => resolve(DUMMY_GROOM), 500)
  )
  return data
}
