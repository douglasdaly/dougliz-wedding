// api/users.ts
import { NuxtAxiosInstance } from '@nuxtjs/axios'

import { IUsersAPI } from './types'
import { User } from '~/types'

const UsersAPI = function (axios: NuxtAxiosInstance): IUsersAPI {
  return {
    async getCurrent (): Promise<User|undefined> {
      const res = await axios.get('/users/me')
      if (res.status === 200) {
        return res.data
      }
    },
  }
}

export default UsersAPI
