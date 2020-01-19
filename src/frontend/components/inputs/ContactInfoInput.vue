<template>
  <v-container fluid class="pa-0">
    <!-- Titles -->
    <v-list-item v-if="title || subtitle"
      class="px-0"
    >
      <v-list-item-content class="py-0">
        <v-list-item-title v-if="title">
          <span class="title heading-text">{{ title }}</span>
        </v-list-item-title>
        <v-list-item-subtitle v-if="subtitle">
          <span class="subtitle-2">
            {{ subtitle }}
          </span>
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <!-- Email -->
    <v-row>
      <v-col v-if="showIcons"
        cols="auto"
        class="mt-2"
      >
        <v-icon>mdi-email</v-icon>
      </v-col>
      <v-col class="py-0">
        <v-text-field
          v-model="contact.email"
          label="Email address"
          required
          :error-messages="emailErrors"
          @input="$v.contact.email.$touch()"
          @blur="$v.contact.email.$touch()"
        ></v-text-field>
      </v-col>
    </v-row>

    <!-- Phone numbers -->
    <v-row>
      <v-col v-if="showIcons"
        cols="auto"
        class="mt-2"
      >
        <v-icon>mdi-phone</v-icon>
      </v-col>
      <v-col class="py-0">
        <v-row>
          <!-- Home -->
          <v-col class="py-0">
            <v-text-field
              v-model="contact.phone"
              label="Home phone"
              :error-messages="phoneErrors"
              @input="$v.contact.phone.$touch()"
              @blur="$v.contact.phone.$touch()"
            ></v-text-field>
          </v-col>

          <!-- Mobile (bigger screens) -->
          <v-col v-if="$vuetify.breakpoint.mdAndUp"
            class="py-0"
          >
            <v-text-field
              v-model="contact.mobile"
              label="Cell phone"
              :error-messages="mobileErrors"
              @input="$v.contact.mobile.$touch()"
              @blur="$v.contact.mobile.$touch()"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <!-- Mobile (smaller screens) -->
    <v-row v-if="$vuetify.breakpoint.smAndDown">
      <v-col v-if="showIcons"
        cols="auto"
        class="mt-2"
      >
        <v-icon>mdi-cellphone</v-icon>
      </v-col>
      <v-col class="py-0">
        <v-text-field
          v-model="contact.mobile"
          label="Cell phone"
          :error-messages="mobileErrors"
          @input="$v.contact.mobile.$touch()"
          @blur="$v.contact.mobile.$touch()"
        ></v-text-field>
      </v-col>
    </v-row>

    <!-- Other contact method -->
    <v-row v-if="showOther">
      <v-col
        cols="auto"
        class="px-2 mt-1"
      >
        <v-btn
          fab
          x-small
          color="primary"
          @click="setShowOther(false)"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-col>
      <v-col class="py-0">
        <v-row>
          <v-col cols="12" :md=true
            class="py-0"
          >
            <v-combobox
              ref="otherStart"
              v-model="contact.otherType"
              :items="otherTypes"
              label="Other method"
              :error-messages="otherTypeErrors"
              @input="$v.contact.otherType.$touch()"
              @blur="$v.contact.otherType.$touch()"
            ></v-combobox>
          </v-col>
          <v-col cols="12" :md=true
            class="py-0"
          >
            <v-text-field
              v-model="contact.otherValue"
              :label="otherValueLabel"
              :error-messages="otherValueErrors"
              @input="$v.contact.otherValue.$touch()"
              @blur="$v.contact.otherValue.$touch()"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-row v-else>
      <v-col class="pl-1">
        <v-btn
          color="primary"
          class="px-2"
          text
          @click="setShowOther(true)"
        >
          <v-row align="center">
            <v-col cols="auto"
              class="py-0"
            >
              <v-icon>mdi-comment-plus</v-icon>
            </v-col>
            <v-col align="center" class="py-0 pl-2">
              Add another method
            </v-col>
          </v-row>
        </v-btn>
      </v-col>
    </v-row>

    <!-- Preferred contact method -->
    <v-row>
      <v-col :class="showOther ? 'py-0' : 'pb-0'">
        <span class="caption">
          {{ preferredText }}
        </span>
      </v-col>
    </v-row>
    <v-row>
      <v-col v-if="showIcons"
        cols="auto"
        class="pb-0"
      >
        <v-icon>mdi-account-question</v-icon>
      </v-col>
      <v-col class="py-0">
        <v-input
          dense
          :error-messages="preferredMethodErrors"
          @click="$v.contact.preferredMethod.$touch()"
        >
          <v-chip-group
            v-model="contact.preferredMethod"
            active-class="primary"
            mandatory
            column
          >
            <v-chip v-for="(enabled, method) in allowedPreferredMethods"
              :key="method"
              :value="method"
              :disabled="!enabled"
              filter
            >
              {{ method }}
            </v-chip>
          </v-chip-group>
        </v-input>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Model, Prop, Vue } from 'nuxt-property-decorator'

import { required } from 'vuelidate/lib/validators'

import { ContactInfo, Dict } from '~/types'

import { contactConstants } from '~/utils/constants'
import { validPhone } from '~/utils/validators'

@Component
export default class ContactInfoInput extends Vue {
  @Model('change', { type: Object }) contact!: ContactInfo
  @Prop({ type: String }) title?: string
  @Prop({ type: String }) subtitle?: string
  @Prop({ type: Boolean, default: true }) showIcons!: boolean
  @Prop({ type: String }) namePrefix?: string

  // Data
  valid: boolean = false
  showOther: boolean = false
  otherTypes: string[] = contactConstants.other.types

  // Hooks
  created () {
    if (this.contact.otherType || this.contact.otherValue) {
      this.showOther = true
    }
    this.valid = this.formIsValid(false)
  }

  // Computed
  get allowedPreferredMethods () {
    const rv: Dict<boolean> = {
      Email: true,
      Phone: false,
      Mobile: false
    }
    if (this.contact.phone) {
      rv.Phone = true
    }
    if (this.contact.mobile) {
      rv.Mobile = true
    }
    if (this.showOther) {
      let otherName: string = "Other"
      let otherValue = false
      if (this.contact.otherType
          && this.otherTypes.includes(this.contact.otherType)) {
        otherName = this.contact.otherType
      }
      if (this.contact.otherValue) {
        otherValue = true
      }
      rv[otherName] = otherValue
    }
    return rv
  }

  get otherValueLabel () {
    if (this.contact.otherType
        && this.otherTypes.includes(this.contact.otherType)) {
      return `${this.contact.otherType} ID`
    }
    return "Other ID"
  }

  get preferredText (): string {
    let rv = ""
    if (this.namePrefix) {
      rv += `${this.namePrefix}'s preferred`
    } else {
      rv += 'Preferred'
    }
    rv += " contact method"
    return rv
  }

  // Methods
  formIsValid (touch: boolean = true): boolean {
    if (this.$v.contact) {
      touch && this.$v.contact.$touch()
      if (!this.$v.contact.$invalid) {
        return true
      }
    }
    return false
  }

  setShowOther (value: boolean) {
    this.showOther = value
  }

  // Vuelidate
  validations () {
    return {
      contact: {
        email: {
          required
        },
        phone: {
          validPhone
        },
        mobile: {
          validPhone
        },
        otherType: {},
        otherValue: {},
        preferredMethod: {
          required
        }
      }
    }
  }

  get emailErrors () {
    const errors: string[] = []
    if (this.$v.contact && this.$v.contact.email) {
      if (!this.$v.contact.email.$dirty) return errors
      !this.$v.contact.email.required && errors.push("Email address is required")
    }
    return errors
  }

  get phoneErrors () {
    const errors: string[] = []
    if (this.$v.contact && this.$v.contact.phone) {
      if (!this.$v.contact.phone.$dirty) return errors
    }
    return errors
  }

  get mobileErrors () {
    const errors: string[] = []
    if (this.$v.contact && this.$v.contact.mobile) {
      if (!this.$v.contact.mobile.$dirty) return errors
    }
    return errors
  }

  get otherTypeErrors () {
    const errors: string[] = []
    if (this.$v.contact && this.$v.contact.otherType) {
      if (!this.$v.contact.otherType.$dirty) return errors
    }
    return errors
  }

  get otherValueErrors () {
    const errors: string[] = []
    if (this.$v.contact && this.$v.contact.otherValue) {
      if (!this.$v.contact.otherValue.$dirty) return errors
    }
    return errors
  }

  get preferredMethodErrors () {
    const errors: string[] = []
    if (this.$v.contact && this.$v.contact.preferredMethod) {
      if (!this.$v.contact.preferredMethod.$dirty) return errors
      !this.$v.contact.preferredMethod.required && errors.push("Preferred contact method is required")
    }
    return errors
  }
}
</script>
