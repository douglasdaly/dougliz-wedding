// env.ts

// Environment variables
// - General Application
export const NODE_ENV = process.env.NODE_ENV

let envDebug
if (NODE_ENV) {
  envDebug = NODE_ENV === 'development'
} else {
  envDebug = false
}
export const DEBUG = envDebug

export const NUXT_APP_ENV = process.env.NUXT_APP_ENV

// - Backend API
let envApiUrl = ''
if (NUXT_APP_ENV === 'docker') {
  envApiUrl = 'http://backend'
} else {
  envApiUrl = 'http://localhost:5000'
}
export const API_URL = envApiUrl

// Aggregated object
const env = {
  API_URL,
  DEBUG,
  NODE_ENV,
  NUXT_APP_ENV,
}

export default env
