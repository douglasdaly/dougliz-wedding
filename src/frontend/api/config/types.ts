// api/config/types.ts
import { Setting } from '~/types/config'

export interface ISettingsAPI {
  createSetting<T> (setting: Setting<T>): Promise<Setting<T>>
  getSettings (skip?: number, limit?: number): Promise<Setting<any>[]>
  getSettingValue<T> (name: string): Promise<Setting<T>>
  getSettingId<T> (id: string): Promise<Setting<T>>
  updateSettingId<T> (id: string, data: object): Promise<Setting<T>>
  updateSetting<T> (name: string, value?: T): Promise<Setting<T>>
  deleteSettingId<T> (id: string): Promise<Setting<T>>
}
