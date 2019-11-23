// index.ts
import { NuxtAxiosInstance } from '@nuxtjs/axios'

import { IAPI } from './types'

import ConfigAPI from './config'
import EventsAPI from './events'
import LoginAPI from './login'
import NamesAPI from './names'
import PeopleAPI from './people'
import UsersAPI from './users'

import { saveLocalToken, getLocalToken } from '~/utils/tokens'

const API = function (axios: NuxtAxiosInstance): IAPI {
  return {
    // Sub-modules
    config: ConfigAPI(axios),
    events: EventsAPI(axios),
    login: LoginAPI(axios),
    names: NamesAPI(axios),
    people: PeopleAPI(axios),
    users: UsersAPI(axios),

    // Additional Functions
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
};

export default API;
