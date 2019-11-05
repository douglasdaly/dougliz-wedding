// api/wedding.ts
import { NuxtAxiosInstance } from '@nuxtjs/axios'

import { Person } from '~/types'

const DUMMY_BRIDE: Person = {
  name: {
    first: 'The',
    last: 'Bride'
  },
  contact: {
    email: 'thebride@example.com',
    preferredMethod: 'email'
  }
}

const DUMMY_GROOM: Person = {
  name: {
    first: 'The',
    last: 'Groom',
  },
  contact: {
    email: 'thegroom@example.com',
    preferredMethod: 'email'
  }
}

export const getBride = async (): Promise<Person> => {
  const data = await new Promise<Person>(resolve =>
    setTimeout(() => resolve(DUMMY_BRIDE), 500)
  )
  return data
}

export const getGroom = async (): Promise<Person> => {
  const data = await new Promise<Person>(resolve =>
    setTimeout(() => resolve(DUMMY_GROOM), 500)
  )
  return data
}


const WeddingAPI = function (axios: NuxtAxiosInstance) {
  return {
    getPartyName: async (role: string): Promise<Person[] | undefined> => {
      const res = await axios.get(`/wedding/info/party/${role.toLowerCase()}`)
      if (res.status === 200) {
        return res.data
      }
    }
  }
}

export default WeddingAPI
