// api/types.ts
import { User } from '~/types'

export interface IAPI {
  config: IConfigAPI,
  login: ILoginAPI,
  users: IUsersAPI,

  userLogin(username: string, password: string): Promise<User|undefined>,
  tokenLogin(token?: string): Promise<User|undefined>,
}

export interface IConfigAPI {
  getSetting(name: string): Promise<any>,
}

export interface ILoginAPI {
  getToken (username: string, password: string): Promise<string|undefined>,
  testToken (token: string): Promise<User|undefined>,
}

export interface IUsersAPI {
  getCurrent (): Promise<User|undefined>,
}
