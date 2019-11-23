// api/names.ts
import { NuxtAxiosInstance } from '@nuxtjs/axios'

import { INamesAPI } from './types'

const NamesAPI = function (axios: NuxtAxiosInstance): INamesAPI {
  return {
    async createName (name) {
      const res = await axios.post('/names', name);
      if (res.status === 200) {
        return res.data;
      }
    },

    async getNameById (nameId) {
      const res = await axios.get(`/names/${nameId}`);
      if (res.status === 200) {
        return res.data;
      }
    },

    async getNames (skip, limit) {
      const res = await axios.get('/names', { params: { skip, limit } });
      if (res.status === 200) {
        return res.data;
      }
    },

    async updateName (nameId, data) {
      const res = await axios.put(`/names/${nameId}`, data);
      if (res.status === 200) {
        return res.data;
      }
    },
  }
};

export default NamesAPI;
