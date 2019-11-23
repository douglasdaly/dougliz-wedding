// api/config.ts
import { NuxtAxiosInstance } from '@nuxtjs/axios'

import { IConfigAPI } from '../types'
import SettingsAPI from './settings'

const ConfigAPI = function (axios: NuxtAxiosInstance): IConfigAPI {
  return {
    settings: SettingsAPI(axios),
  };
};

export default ConfigAPI;
