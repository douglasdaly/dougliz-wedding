// nuxt.config.ts
import { Context } from 'vm'

const VuetifyLoaderPlugin = require('vuetify-loader/lib/plugin')

export default {
  mode: 'spa',
  /*
  ** Headers of the page
  */
  head: {
    titleTemplate: (titleChunk: string | undefined) => {
      return titleChunk ? `${titleChunk} - Doug & Liz` : 'Doug & Liz'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Doug & Liz\'s Wedding' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Tangerine' },
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },
  /*
  ** Global CSS
  */
  css: [
    '~/assets/css/main.css'
  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
    '@nuxtjs/eslint-module',
    '@nuxt/typescript-build'
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    '@nuxtjs/axios'
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    '~/plugins/get-api',
    '~/plugins/vuelidate',
    '~/plugins/vuetify'
  ],
  /*
  ** Axios configuration
  */
  axios: {
    prefix: '/api',
    host: 'localhost',
    port: 5000
  },
  /*
  ** Proxy configuration
  */
  proxy: {},
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend (config: any, ctx: Context) {
      // Run ESLint on save
      if (ctx.isDev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(ts|js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    },
    plugins: [
      new VuetifyLoaderPlugin()
    ],
    loaders: {
      vue: {
        transformAssetUrls: {
          video: ['src', 'poster'],
          source: 'src',
          img: 'src',
          image: 'xlink:href',
          'v-img': 'src',
          'v-parallax': 'src'
        }
      }
    }
  }
}
