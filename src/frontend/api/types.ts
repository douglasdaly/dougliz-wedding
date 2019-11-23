// api/types.ts
import { ISettingsAPI } from './config/types'

import { Event, Name, Person, User } from '~/types'

export interface IAPI {
  config: IConfigAPI
  events: IEventsAPI
  login: ILoginAPI
  names: INamesAPI
  people: IPeopleAPI
  users: IUsersAPI

  userLogin(username: string, password: string): Promise<User|undefined>
  tokenLogin(token?: string): Promise<User|undefined>
}

export interface IConfigAPI {
  settings: ISettingsAPI
}

export interface IEventsAPI {
  createEvent (event: Event): Promise<Event>
  getUpcomingEvents (skip?: number, limit?: number): Promise<Event[]>
  getAllEvents (skip?: number, limit?: number): Promise<Event[]>
  getEvent (eventId: string): Promise<Event>
  updateEvent (eventId: string, data: object): Promise<Event>
  deleteEvent (eventId: string): Promise<Event>
}

export interface ILoginAPI {
  getToken (username: string, password: string): Promise<string|undefined>
  testToken (token: string): Promise<User|undefined>
}

export interface INamesAPI {
  createName (name: Name): Promise<Name>
  getNameById (nameId: string): Promise<Name>
  getNames (skip?: number, limit?: number): Promise<Name[]>
  updateName (nameId: string, data: object): Promise<Name>
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
  createUser (user: User): Promise<User>
  createUserOpen (user: User): Promise<User>
  getUsers (skip?: number, limit?: number): Promise<User[]>
  getUser (userId: string): Promise<User>
  getCurrent (): Promise<User|undefined>
  updateUser (userId: string, data: object): Promise<User>
  updateCurrent (password: string, data: object): Promise<User>
  deleteUser (userId: string): Promise<User>
}
