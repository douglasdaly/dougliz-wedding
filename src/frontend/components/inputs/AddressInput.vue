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

    <!-- Country -->
    <v-row>
      <v-col v-if="showIcons"
        cols="auto"
        class="mt-2"
      >
        <v-icon>mdi-earth</v-icon>
      </v-col>
      <v-col class="py-0">
        <v-select
          v-model="address.country"
          :items="countries"
          :menu-props="{ top: true, offsetY: true }"
          label="Country"
          required
          :error-messages="countryErrors"
          @change="$v.address.country.$touch()"
          @blur="$v.address.country.$touch()"
        ></v-select>
      </v-col>
    </v-row>

    <!-- Address lines -->
    <v-row>
      <v-col v-if="showIcons"
        cols="auto"
        class="mt-2"
      >
        <v-icon>mdi-home</v-icon>
      </v-col>
      <v-col class="py-0">
        <!-- Line 1 -->
        <v-row>
          <v-col class="py-0">
            <v-text-field
              v-model="address.line1"
              label="Address Line 1"
              required
              :error-messages="line1Errors"
              @input="$v.address.line1.$touch()"
              @blur="$v.address.line1.$touch()"
            ></v-text-field>
          </v-col>
        </v-row>

        <!-- Line 2 -->
        <v-row>
          <v-col class="py-0">
            <v-text-field
              v-model="address.line2"
              label="Address Line 2"
              :error-messages="line2Errors"
              @input="$v.address.line2.$touch()"
              @blur="$v.address.line2.$touch()"
            ></v-text-field>
          </v-col>
        </v-row>

        <!-- Line 3 -->
        <v-row v-if="address.line2">
          <v-col class="py-0">
            <v-text-field
              v-model="address.line3"
              label="Address Line 3"
              :error-messages="line3Errors"
              @input="$v.address.line3.$touch()"
              @blur="$v.address.line3.$touch()"
            ></v-text-field>
          </v-col>
        </v-row>

        <!-- City/State/Zip -->
        <v-row>
          <v-col cols="12" :sm=true
            class="py-0"
          >
            <v-text-field
              v-model="address.city"
              label="City"
              required
              :error-messages="cityErrors"
              @input="$v.address.city.$touch()"
              @blur="$v.address.city.$touch()"
            ></v-text-field>
          </v-col>
          <v-col v-if="isRequiredUS"
            cols="6" :sm=true
            class="py-0"
          >
            <v-select
              v-model="address.state"
              :items="states"
              label="State"
              required
              :error-messages="stateErrors"
              @change="$v.address.state.$touch()"
              @blur="$v.address.state.$touch()"
            ></v-select>
          </v-col>
          <v-col v-if="isRequiredUS"
            cols="6" :sm=true
            class="py-0"
          >
            <v-text-field
              v-model="address.zipCode"
              label="Zip"
              required
              :error-messages="zipCodeErrors"
              @input="$v.address.zipCode.$touch()"
              @blur="$v.address.zipCode.$touch()"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import {
  Component,
  Model,
  Prop,
  Vue
} from 'nuxt-property-decorator'

import { required, requiredIf } from 'vuelidate/lib/validators'

import { Address } from '~/types'
import { validZip } from '~/utils/validators'

import { geographyConstants } from '~/utils/constants'

@Component
export default class AddressInput extends Vue {
  @Model('change', { type: Object }) address!: Address
  @Prop({ type: String, required: false }) title?: string
  @Prop({ type: String, required: false }) subtitle?: string
  @Prop({ type: Boolean, default: true }) showIcons!: boolean

  // Data
  valid: boolean = false
  countries: string[] = geographyConstants.country.names
  states: string[] = geographyConstants.state.codes

  // Hooks
  created () {
    if (!this.address.country) {
      this.address.country = "United States";
    }
    this.valid = this.formIsValid(false);
  }

  // Computed
  get isRequiredUS (): boolean {
    if (this.address.country) {
      return this.address.country === "United States";
    }
    return false;
  }

  // Vuelidate
  validations () {
    return {
      address: {
        country: {
          required
        },
        line1: {
          required
        },
        line2: {},
        line3: {},
        city: {
          required
        },
        state: {
          required: requiredIf(() => this.isRequiredUS)
        },
        zipCode: {
          required: requiredIf(() => this.isRequiredUS),
          validZip
        }
      }
    }
  }

  get countryErrors (): string[] {
    const errors: string[] = []
    if (this.$v.address && this.$v.address.country) {
      if (!this.$v.address.country.$dirty) return errors
      !this.$v.address.country.required && errors.push("Country is required")
    }
    return errors
  }

  get line1Errors (): string[] {
    const errors: string[] = []
    if (this.$v.address && this.$v.address.line1) {
      if (!this.$v.address.line1.$dirty) return errors
      !this.$v.address.line1.required && errors.push("Address is required")
    }
    return errors
  }

  get line2Errors (): string[] {
    const errors: string[] = []
    if (this.$v.address && this.$v.address.line2) {
      if (!this.$v.address.line2.$dirty) return errors
    }
    return errors
  }

  get line3Errors (): string[] {
    const errors: string[] = []
    if (this.$v.address && this.$v.address.line3) {
      if (!this.$v.address.line3.$dirty) return errors
    }
    return errors
  }

  get cityErrors (): string[] {
    const errors: string[] = []
    if (this.$v.address && this.$v.address.city) {
      if (!this.$v.address.city.$dirty) return errors
      !this.$v.address.city.required && errors.push("City is required")
    }
    return errors
  }

  get stateErrors (): string[] {
    const errors: string[] = []
    if (this.$v.address && this.$v.address.state) {
      if (!this.$v.address.state.$dirty) return errors
      !this.$v.address.state.required && errors.push("State is required")
    }
    return errors
  }

  get zipCodeErrors (): string[] {
    const errors: string[] = []
    if (this.$v.address && this.$v.address.zipCode) {
      if (!this.$v.address.zipCode.$dirty) return errors
      !this.$v.address.zipCode.required && errors.push("Zip code is required")
      !this.$v.address.zipCode.validZip && errors.push("Invalid zip code")
    }
    return errors
  }

  // Methods
  formIsValid (touch: boolean = true): boolean {
    if (this.$v.address) {
      touch && this.$v.address.$touch()
      if (!this.$v.address.$invalid) {
        return true
      }
    }
    return false;
  }

  reset () {
    this.$v.$reset();
  }
}
</script>
