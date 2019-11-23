// api/config/settings.ts
import { NuxtAxiosInstance } from '@nuxtjs/axios'

import { ISettingsAPI } from './types'

const SettingsAPI = function (axios: NuxtAxiosInstance): ISettingsAPI {
  return {
    async createSetting (setting) {
      const res = await axios.post('/config/settings', setting);
      if (res.status === 200) {
        return res.data;
      }
    },

    async getSettings (skip, limit) {
      const res = await axios.get('/config/settings', { params: { skip, limit } });
      if (res.status === 200) {
        return res.data;
      }
    },

    async getSettingValue (name) {
      const res = await axios.get(`/config/settings/${name}`);
      if (res.status === 200) {
        return res.data;
      }
    },

    async getSettingId (id) {
      const res = await axios.get(`/config/settings/id/${id}`);
      if (res.status === 200) {
        return res.data;
      }
    },

    async updateSettingId (id, data) {
      const res = await axios.put(`/config/settings/id/${id}`, data);
      if (res.status === 200) {
        return res.data;
      }
    },

    async updateSetting (name, value) {
      const res = await axios.put(`/config/settings/${name}`, value);
      if (res.status === 200) {
        return res.data;
      }
    },

    async deleteSettingId (id) {
      const res = await axios.delete(`/config/settings/id/${id}`);
      if (res.status === 200) {
        return res.data;
      }
    }
  };
};

export default SettingsAPI;
