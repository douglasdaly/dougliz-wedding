// api/login.ts
import { NuxtAxiosInstance } from '@nuxtjs/axios'

import { User } from '~/types'

export function getAuthHeaders (token: string) {
  return {
    headers: {
      Authorization: `Bearer ${token}`
    }
  }
}

const LoginAPI = function (axios: NuxtAxiosInstance) {
  return {
    async getToken (username: string, password: string): Promise<string|undefined> {
      const params = new URLSearchParams()
      params.append('username', username)
      params.append('password', password)

      const res = await axios.post('/login/login/access-token', params)
      if (res.status === 200) {
        return res.data.accessToken
      }
    },

    async testToken (token: string): Promise<User|undefined> {
      const res = await axios.post('/login/login/test-token', getAuthHeaders(token))
      if (res.status === 200) {
        return res.data
      }
    },
  }
}

export default LoginAPI
