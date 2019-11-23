// api/users.ts
import { NuxtAxiosInstance } from '@nuxtjs/axios'

import { IUsersAPI } from './types'

const UsersAPI = function (axios: NuxtAxiosInstance): IUsersAPI {
  return {
    async createUser (user) {
      const res = await axios.post('/users', user);
      if (res.status === 200) {
        return res.data;
      }
    },

    async createUserOpen (user) {
      const res = await axios.post('/users/open', user);
      if (res.status === 200) {
        return res.data;
      }
    },

    async getUsers (skip, limit) {
      const res = await axios.get('/users', { params: { skip, limit } });
      if (res.status === 200) {
        return res.data;
      }
    },

    async getUser (userId) {
      const res = await axios.get(`/users/id/${userId}`);
      if (res.status === 200) {
        return res.data;
      }
    },

    async getCurrent () {
      const res = await axios.get('/users/me')
      if (res.status === 200) {
        return res.data
      }
    },

    async updateUser (userId, data) {
      const res = await axios.put(`/users/id/${userId}`, data);
      if (res.status === 200) {
        return res.data;
      }
    },

    async updateCurrent (password, data) {
      const res = await axios.put('/users/me', {
        currentPassword: password,
        updatedUser: data,
      });
      if (res.status === 200) {
        return res.data;
      }
    },

    async deleteUser (userId) {
      const res = await axios.delete(`/users/id/${userId}`);
      if (res.status === 200) {
        return res.data;
      }
    }
  }
};

export default UsersAPI;
