// index.ts
import { NuxtAxiosInstance } from '@nuxtjs/axios'

import { IAPI } from './types'
import ConfigAPI from './config'
import LoginAPI from './login'
import UsersAPI from './users'

import { saveLocalToken, getLocalToken } from '~/utils/tokens'

const API = function (axios: NuxtAxiosInstance): IAPI {
  return {
    // Sub-modules
    config: ConfigAPI(axios),
    login: LoginAPI(axios),
    users: UsersAPI(axios),

    // Functions
    async userLogin(username: string, password: string) {
      const token = await this.login.getToken(username, password)
      if (token) {
        saveLocalToken(token)
        axios.setHeader('Authorization', `Bearer ${token}`)
        return this.users.getCurrent()
      }
    },

    async tokenLogin(token?: string) {
      if (!token) {
        const localToken = getLocalToken()
        if (localToken) {
          token = localToken
        }
      }
      if (token) {
        const valid = await this.login.testToken(token)
        if (valid) {
          saveLocalToken(token)
          axios.setHeader('Authorization', `Bearer ${token}`)
          return this.users.getCurrent()
        }
      }
    },
  }
}

export default API
