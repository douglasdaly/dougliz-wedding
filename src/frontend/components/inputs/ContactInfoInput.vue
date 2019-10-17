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

    <!-- Email -->
    <v-row>
      <v-col v-if="showIcons"
        cols="auto"
      >
        <v-icon>mdi-email</v-icon>
      </v-col>
      <v-col :class="{ 'py-0': true, 'mt-1': showIcons }">
        <v-text-field
          v-model="contact.email"
          label="Email address"
          dense
          required
        ></v-text-field>
      </v-col>
    </v-row>

    <!-- Phone numbers -->
    <v-row>
      <v-col v-if="showIcons"
        cols="auto"
      >
        <v-icon>mdi-phone</v-icon>
      </v-col>
      <v-col :class="{ 'py-0': true, 'mt-1': showIcons }">
        <v-row>
          <!-- Home -->
          <v-col class="py-0">
            <v-text-field
              v-model="contact.phone"
              label="Home phone"
              dense
            ></v-text-field>
          </v-col>

          <!-- Mobile (bigger screens) -->
          <v-col v-if="$vuetify.breakpoint.mdAndUp"
            class="py-0"
          >
            <v-text-field
              v-model="contact.mobile"
              label="Cell phone"
              dense
            ></v-text-field>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <!-- Mobile (smaller screens) -->
    <v-row v-if="$vuetify.breakpoint.smAndDown">
      <v-col v-if="showIcons"
        cols="auto"
      >
        <v-icon>mdi-cellphone</v-icon>
      </v-col>
      <v-col :class="{ 'py-0': true, 'mt-1': showIcons }">
        <v-text-field
          v-model="contact.mobile"
          label="Cell phone"
          dense
        ></v-text-field>
      </v-col>
    </v-row>

    <!-- Other contact method -->
    <v-row v-if="showOther">
      <v-col
        cols="auto"
        class="px-2"
      >
        <v-btn
          fab
          x-small
          color="primary"
          @click="showOther = false"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-col>
      <v-col class="pt-2 pb-0">
        <v-row>
          <v-col cols="12" :md=true
            class="py-0"
          >
            <v-combobox
              v-model="contact.otherType"
              :items="otherTypes"
              label="Other method"
              dense
            ></v-combobox>
          </v-col>
          <v-col cols="12" :md=true
            class="py-0"
          >
            <v-text-field
              v-model="contact.otherValue"
              label="Other ID"
              dense
            ></v-text-field>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-row v-else>
      <v-col class="pl-1 py-0">
        <v-btn
          color="primary"
          class="px-2"
          text
          @click="showOther = true"
        >
          <v-row align="center">
            <v-col cols="auto"
              class="py-0"
            >
              <v-icon>mdi-comment-plus</v-icon>
            </v-col>
            <v-col class="pl-2">
              Add another method
            </v-col>
          </v-row>
        </v-btn>
      </v-col>
    </v-row>

    <!-- Preferred contact method -->
    <template v-if="allowedPreferredMethods.length > 1">
      <v-row>
        <v-col class="py-0">
          <span class="caption">
            Preferred contact method
          </span>
        </v-col>
      </v-row>
      <v-row>
        <v-col v-if="showIcons"
          cols="auto"
        >
          <v-icon>mdi-account-question</v-icon>
        </v-col>
        <v-col class="py-0">
          <v-row>
            <v-col class="py-0">
              <v-chip-group
                v-model="contact.preferredMethod"
                active-class="primary"
                mandatory
                column
              >
                <v-chip v-for="method in allowedPreferredMethods"
                  :key="method"
                  :value="method"
                >
                  {{ method }}
                </v-chip>
              </v-chip-group>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </template>
  </v-container>
</template>

<script lang="ts">
import { Component, Model, Prop, Vue } from 'nuxt-property-decorator'

import { ContactInfo } from '~/types'

import { contactConstants } from '~/utils/constants'

@Component
export default class ContactInfoInput extends Vue {
  @Model('change', { type: Object }) contact!: ContactInfo
  @Prop({ type: String }) title: string | undefined
  @Prop({ type: String }) subtitle: string | undefined
  @Prop({ type: Boolean, default: true }) showIcons: boolean

  // Data
  showOther: boolean = false
  otherTypes: string[] = contactConstants.other.types

  // Hooks
  created () {
    if (this.contact.otherType || this.contact.otherValue) {
      this.showOther = true
    }
  }

  // Computed
  get allowedPreferredMethods () {
    const rv: string[] = ['Email']
    if (this.contact.phone) {
      rv.push('Phone')
    }
    if (this.contact.mobile) {
      rv.push('Mobile')
    }
    if (this.showOther && this.contact.otherType) {
      rv.push(this.contact.otherType)
    }
    return rv
  }
}
</script>
