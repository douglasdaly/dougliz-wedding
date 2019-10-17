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
              dense
            ></v-combobox>
          </v-col>

          <!-- First name -->
          <v-col cols="12" :sm=true
            class="py-0"
          >
            <v-text-field
              v-model="name.first"
              label="First name"
              dense
              required
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
              dense
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
              dense
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
              dense
            ></v-combobox>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Model, Prop, Vue } from 'nuxt-property-decorator'

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
  nameSuffixes: string[] = nameConstants.suffixes
  nameTitles: string[] = nameConstants.prefixes

  // Hooks
  create () {
    if (name.middle && this.middleName === undefined) {
      this.middleName = true
    }
    if (name.short && this.nickName === undefined) {
      this.nickName = true
    }
  }
}
</script>
