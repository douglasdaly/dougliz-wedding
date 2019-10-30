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
              v-model="nameModel.prefix"
              :items="nameTitles"
              label="Title"
              :error-messages="titleErrors"
              @input="$v.nameModel.title.$touch()"
              @blur="$v.nameModel.title.$touch()"
            ></v-combobox>
          </v-col>

          <!-- First name -->
          <v-col cols="12" :sm=true
            class="py-0"
          >
            <v-text-field
              v-model="nameModel.first"
              label="First name"
              required
              :error-messages="firstErrors"
              @input="$v.nameModel.first.$touch()"
              @blur="$v.nameModel.first.$touch()"
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
              v-model="nameModel.short"
              label="Nickname"
              :error-messages="shortErrors"
              @input="$v.nameModel.short.$touch()"
              @blur="$v.nameModel.short.$touch()"
            ></v-text-field>
          </v-col>

          <!-- Middle name -->
          <v-col v-if="middleName"
            cols="12"
            :sm="true"
            class="py-0"
          >
            <v-text-field
              v-model="nameModel.middle"
              label="Middle name"
              dense
              @input="$v.nameModel.middle.$touch()"
              @blur="$v.nameModel.middle.$touch()"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <!-- Last name -->
          <v-col cols="12" :sm="true"
            class="py-0"
          >
            <v-text-field
              v-model="nameModel.last"
              label="Last name"
              required
              :error-messages="lastErrors"
              @input="$v.nameModel.last.$touch()"
              @blur="$v.nameModel.last.$touch()"
            ></v-text-field>
          </v-col>

          <!-- Suffix -->
          <v-col cols="12" sm="auto"
            class="py-0"
          >
            <v-combobox
              v-model="nameModel.suffix"
              :items="nameSuffixes"
              label="Suffix"
              :error-messages="suffixErrors"
              @input="$v.nameModel.suffix.$touch()"
              @blur="$v.nameModel.suffix.$touch()"
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
  @Model('change', { type: Object }) nameModel!: Name
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
    if (this.nameModel.middle && this.middleName === undefined) {
      this.middleName = true
    }
    if (this.nameModel.short && this.nickName === undefined) {
      this.nickName = true
    }
    this.valid = this.formIsValid(false)
  }

  // Methods
  formIsValid (touch: boolean = true): boolean {
    if (this.$v.nameModel) {
      touch && this.$v.nameModel.$touch()
      if (!this.$v.nameModel.$invalid) {
        return true
      }
    }
    return false
  }

  // Vuelidate
  validations () {
    return {
      nameModel: {
        title: {},
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

  get titleErrors () {
    const errors: string[] = []
    if (this.$v.nameModel && this.$v.nameModel.title) {
      if (!this.$v.nameModel.title.$dirty) return errors
    }
    return errors
  }

  get firstErrors () {
    const errors: string[] = []
    if (this.$v.nameModel && this.$v.nameModel.first) {
      if (!this.$v.nameModel.first.$dirty) return errors
      !this.$v.nameModel.first.required && errors.push("First name is required")
    }
    return errors
  }

  get middleErrors () {
    const errors: string[] = []
    if (this.$v.nameModel && this.$v.nameModel.middle) {
      if (!this.$v.nameModel.middle.$dirty) return errors
    }
    return errors
  }

  get lastErrors () {
    const errors: string[] = []
    if (this.$v.nameModel && this.$v.nameModel.last) {
      if (!this.$v.nameModel.last.$dirty) return errors
      !this.$v.nameModel.last.required && errors.push("Last name is required")
    }
    return errors
  }

  get suffixErrors () {
    const errors: string[] = []
    if (this.$v.nameModel && this.$v.nameModel.suffix) {
      if (!this.$v.nameModel.suffix.$dirty) return errors
    }
    return errors
  }

  get shortErrors () {
    const errors: string[] = []
    if (this.$v.nameModel && this.$v.nameModel.short) {
      if (!this.$v.nameModel.short.$dirty) return errors
    }
    return errors
  }
}
</script>
