// types/config.ts
import { Identified, User } from './models'

// - Settings

export interface Setting<T> extends Identified {
  name: string
  value?: T
  required: boolean
  type: string | number
}

// - Permissions

export interface Permission extends Identified {
  name: string
  description?: string
  createDefault: boolean
  readDefault: boolean
  updateDefault: boolean
  deleteDefault: boolean
}

interface PermissionBase extends Identified {
  create: boolean
  read: boolean
  update: boolean
  delete: boolean
}

export interface UserPermission extends PermissionBase {
  permission: Permission
  user: User
}
