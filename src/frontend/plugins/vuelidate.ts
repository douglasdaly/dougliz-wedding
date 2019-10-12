// plugins/vuelidate.ts
import Vue from 'vue'
import Vuelidate from 'vuelidate'
import { Component } from 'nuxt-property-decorator'

Component.registerHooks(['validations'])

Vue.use(Vuelidate)
