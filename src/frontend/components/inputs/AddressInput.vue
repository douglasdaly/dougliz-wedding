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
      >
        <v-icon>mdi-earth</v-icon>
      </v-col>
      <v-col :class="{ 'py-0': true, 'mt-1': showIcons }">
        <v-select
          v-model="address.country"
          :items="countries"
          :menu-props="{ top: true, offsetY: true }"
          label="Country"
          dense
        ></v-select>
      </v-col>
    </v-row>

    <!-- Address lines -->
    <v-row>
      <v-col v-if="showIcons"
        cols="auto"
      >
        <v-icon>mdi-home</v-icon>
      </v-col>
      <v-col :class="{ 'py-0': true, 'mt-1': showIcons }">
        <!-- Line 1 -->
        <v-row>
          <v-col class="py-0">
            <v-text-field
              v-model="address.line1"
              label="Address Line 1"
              dense
              required
            ></v-text-field>
          </v-col>
        </v-row>

        <!-- Line 2 -->
        <v-row>
          <v-col class="py-0">
            <v-text-field
              v-model="address.line2"
              label="Address Line 2"
              dense
            ></v-text-field>
          </v-col>
        </v-row>

        <!-- Line 3 -->
        <v-row v-if="address.line2">
          <v-col class="py-0">
            <v-text-field
              v-model="address.line3"
              label="Address Line 3"
              dense
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
              dense
              required
            ></v-text-field>
          </v-col>
          <v-col v-if="address.country === 'United States'"
            cols="6" :sm=true
            class="py-0"
          >
            <v-select
              v-model="address.state"
              :items="states"
              label="State"
              dense
            ></v-select>
          </v-col>
          <v-col v-if="address.country === 'United States'"
            cols="6" :sm=true
            class="py-0"
          >
            <v-text-field
              v-model="address.zipCode"
              label="Zip"
              dense
            ></v-text-field>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Model, Prop, Vue } from 'nuxt-property-decorator'

import { Address } from '~/types'

import { geographyConstants } from '~/utils/constants'

@Component
export default class AddressInput extends Vue {
  @Model('change', { type: Object }) address!: Address
  @Prop({ type: String }) title: string | undefined
  @Prop({ type: String }) subtitle: string | undefined
  @Prop({ type: Boolean, default: true }) showIcons: boolean

  // Data
  countries: string[] = geographyConstants.country.names
  states: string[] = geographyConstants.state.codes

  // Hooks
  created () {
    if (!this.address.country) {
      this.address.country = "United States"
    }
  }

}
</script>
