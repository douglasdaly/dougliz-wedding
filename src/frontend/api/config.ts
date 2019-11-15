// api/config.ts
import { NuxtAxiosInstance } from '@nuxtjs/axios'

import { IConfigAPI } from './types'

const ConfigAPI = function (axios: NuxtAxiosInstance): IConfigAPI {
  return {
    async getSetting(name: string) {
      const res = await axios.get(`/config/settings/${name}`)
      if (res.status === 200) {
        return res.data
      }
    },
  }
}

export default ConfigAPI
