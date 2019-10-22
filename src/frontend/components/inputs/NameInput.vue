<template>
  <v-container fluid class="pa-0">
    <!-- Titles -->
    <v-list-item v-if="title || subtitle"
      class="px-0"
    >
      <v-list-item-content class="py-0">
        <v-list-item-title v-if="title">
          <span class="title">{{ title }}</span>
        </v-list-item-title>
        <v-list-item-subtitle v-if="subtitle">
          <span class="subtitle-2">
            {{ subtitle }}
          </span>
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <!-- Name inputs -->
    <v-row>
      <v-col v-if="showIcons"
        cols="auto"
        class="mt-2"
      >
        <v-icon>mdi-account</v-icon>
      </v-col>
      <v-col
        :class="{ 'py-0': true, 'mt-1': showIcons }"
      >
        <v-row>
          <!-- Prefix -->
          <v-col cols="12" sm="auto"
            class="py-0"
          >
            <v-combobox
              v-model="name.prefix"
              :items="nameTitles"
              label="Title"
              :error-messages="prefixErrors"
              @input="$v.name.prefix.$touch()"
              @blur="$v.name.prefix.$touch()"
            ></v-combobox>
          </v-col>

          <!-- First name -->
          <v-col cols="12" :sm=true
            class="py-0"
          >
            <v-text-field
              v-model="name.first"
              label="First name"
              required
              :error-messages="firstErrors"
              @input="$v.name.first.$touch()"
              @blur="$v.name.first.$touch()"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row v-if="nickName || middleName">
          <!-- Nickname -->
          <v-col v-if="nickName"
            cols="12"
            :sm="true"
            class="py-0"
          >
            <v-text-field
              v-model="name.short"
              label="Nickname"
              :error-messages="shortErrors"
              @input="$v.name.short.$touch()"
              @blur="$v.name.short.$touch()"
            ></v-text-field>
          </v-col>

          <!-- Middle name -->
          <v-col v-if="middleName"
            cols="12"
            :sm="true"
            class="py-0"
          >
            <v-text-field
              v-model="name.middle"
              label="Middle name"
              dense
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <!-- Last name -->
          <v-col cols="12" :sm="true"
            class="py-0"
          >
            <v-text-field
              v-model="name.last"
              label="Last name"
              required
              :error-messages="lastErrors"
              @input="$v.name.last.$touch()"
              @blur="$v.name.last.$touch()"
            ></v-text-field>
          </v-col>

          <!-- Suffix -->
          <v-col cols="12" sm="auto"
            class="py-0"
          >
            <v-combobox
              v-model="name.suffix"
              :items="nameSuffixes"
              label="Suffix"
              :error-messages="suffixErrors"
              @input="$v.name.suffix.$touch()"
              @blur="$v.name.suffix.$touch()"
            ></v-combobox>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Model, Prop, Vue } from 'nuxt-property-decorator'

import { required } from 'vuelidate/lib/validators'

import { Name } from '~/types'

import { nameConstants } from '~/utils/constants'

@Component
export default class NameInput extends Vue {
  @Model('change', { type: Object }) name!: Name
  @Prop({ type: String }) title: string | undefined
  @Prop({ type: String }) subtitle: string | undefined
  @Prop({ type: Boolean }) nickName: boolean | undefined
  @Prop({ type: Boolean }) middleName: boolean | undefined
  @Prop({ type: Boolean, default: true }) showIcons: boolean

  // Data
  valid: boolean = false
  nameSuffixes: string[] = nameConstants.suffixes
  nameTitles: string[] = nameConstants.prefixes

  // Hooks
  create () {
    if (this.name.middle && this.middleName === undefined) {
      this.middleName = true
    }
    if (this.name.short && this.nickName === undefined) {
      this.nickName = true
    }
    this.valid = this.formIsValid(false)
  }

  // Methods
  formIsValid (touch: boolean = true): boolean {
    if (this.$v.name) {
      touch && this.$v.name.$touch()
      if (!this.$v.name.$invalid) {
        return true
      }
    }
    return false
  }

  // Vuelidate
  validations () {
    return {
      name: {
        prefix: {},
        first: {
          required
        },
        middle: {},
        last: {
          required
        },
        suffix: {},
        short: {}
      }
    }
  }

  get prefixErrors () {
    const errors: string[] = []
    if (this.$v.name && this.$v.name.prefix) {
      if (!this.$v.name.prefix.$dirty) return errors
    }
    return errors
  }

  get firstErrors () {
    const errors: string[] = []
    if (this.$v.name && this.$v.name.first) {
      if (!this.$v.name.first.$dirty) return errors
      !this.$v.name.first.required && errors.push("First name is required")
    }
    return errors
  }

  get middleErrors () {
    const errors: string[] = []
    if (this.$v.name && this.$v.name.middle) {
      if (!this.$v.name.middle.$dirty) return errors
    }
    return errors
  }

  get lastErrors () {
    const errors: string[] = []
    if (this.$v.name && this.$v.name.last) {
      if (!this.$v.name.last.$dirty) return errors
      !this.$v.name.last.required && errors.push("Last name is required")
    }
    return errors
  }

  get suffixErrors () {
    const errors: string[] = []
    if (this.$v.name && this.$v.name.suffix) {
      if (!this.$v.name.suffix.$dirty) return errors
    }
    return errors
  }

  get shortErrors () {
    const errors: string[] = []
    if (this.$v.name && this.$v.name.short) {
      if (!this.$v.name.short.$dirty) return errors
    }
    return errors
  }
}
</script>
