// api/types.ts
import { Person, User } from '~/types'

export interface IAPI {
  config: IConfigAPI
  login: ILoginAPI
  people: IPeopleAPI
  users: IUsersAPI

  userLogin(username: string, password: string): Promise<User|undefined>
  tokenLogin(token?: string): Promise<User|undefined>
}

export interface IConfigAPI {
  getSetting(name: string): Promise<any>
}

export interface ILoginAPI {
  getToken (username: string, password: string): Promise<string|undefined>
  testToken (token: string): Promise<User|undefined>
}

export interface IPeopleAPI {
  createPerson (person: Person): Promise<Person>
  getPeople (skip?: number, limit?: number): Promise<Person[]>
  getPerson (personId: string): Promise<Person>
  getCurrent (): Promise<Person|undefined>
  updatePerson (personId: string, data: object): Promise<Person>
  updateCurrent (data: object): Promise<Person>
  deletePerson (personId: string): Promise<Person>
}

export interface IUsersAPI {
  getCurrent (): Promise<User|undefined>
}
