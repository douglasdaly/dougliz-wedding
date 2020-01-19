// src/plugins/vuetify.js
import '@mdi/font/css/materialdesignicons.css'
import { Context } from 'vm'
import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

export default (ctx: Context) => {
  const vuetify = new Vuetify({
    iconfont: 'mdiSvg',
    theme: {
      themes: {
        light: {
          primary: '#1976D2',
          secondary: '#424242',
          accent: '#82B1FF',
          error: '#FF5252',
          info: '#2196F3',
          success: '#4CAF50',
          warning: '#FFC107',
        },
      }
    },
    breakpoint: {
      thresholds: {
        xs: 340,
        sm: 540,
        md: 800,
        lg: 1280
      },
      scrollBarWidth: 24
    }
  })

  ctx.app.vuetify = vuetify
  // @ts-ignore
  ctx.$vuetify = vuetify.framework
}
