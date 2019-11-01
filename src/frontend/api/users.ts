// api/users.ts
import { NuxtAxiosInstance } from '@nuxtjs/axios'

const UsersAPI = function (axios: NuxtAxiosInstance) {
  return {
    async getCurrent () {
      const res = await axios.get('/users/me')
      if (res.status === 200) {
        return res.data
      }
    },
  }
}

export default UsersAPI
