// api/people.ts
import { NuxtAxiosInstance } from '@nuxtjs/axios'

import { IPeopleAPI } from './types'

const PeopleAPI = function (axios: NuxtAxiosInstance): IPeopleAPI {
  return {
    async createPerson (person) {
      const res = await axios.$post('/people', person);
      if (res.status === 200) {
        return res.data;
      }
    },

    async getPeople (skip?: number, limit?: number) {
      const res = await axios.get('/people', {
        params: { skip, limit }
      });
      if (res.status === 200) {
        return res.data;
      }
    },

    async getPerson (personId) {
      const res = await axios.$get(`/people/${personId}`);
      return res;
    },

    async getCurrent () {
      const res = await axios.$get('/people/me');
      return res
    },

    async updatePerson (personId, data) {
      const res = await axios.$put(`/people/${personId}`, data);
      return res;
    },

    async updateCurrent (data) {
      const res = await axios.$put('/people/me', data);
      return res;
    },

    async deletePerson (personId) {
      const res = await axios.$delete(`/people/${personId}`);
      return res;
    }
  }
};

export default PeopleAPI;
