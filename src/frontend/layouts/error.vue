<template>
  <v-row justify="center">
    <v-dialog v-model="show" persistent max-width="400">
      <v-card
        dark
      >
        <v-card-title class="pt-1">
          <v-container fluid class="pa-0">
            <v-row align="center">
              <v-col cols="auto"
                class="pl-1"
              >
                <v-icon
                  color="error"
                  x-large
                >
                  mdi-alert
                </v-icon>
              </v-col>
              <v-col>
                <v-row>
                  <span class="overline">
                    {{ error.statusCode }} Error
                  </span>
                </v-row>
                <v-row>
                  <span
                    v-if="errorTitle"
                    class="headline"
                  >
                    {{ errorTitle }}
                  </span>
                </v-row>
              </v-col>
            </v-row>
            <v-row v-if="errorMessage">
              <v-divider></v-divider>
            </v-row>
          </v-container>
        </v-card-title>

        <v-card-text v-if="errorMessage">
          {{ errorMessage }}
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="secondary--darken"
            @click="$router.back()"
          >
            <v-icon small class="pr-1">mdi-chevron-left</v-icon>
            Back
          </v-btn>
          <v-btn
            color="primary"
            nuxt
            to="/"
          >
            <v-icon small class="pr-1">mdi-home</v-icon>
            Home
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'nuxt-property-decorator'

import { DEBUG } from '~/env'

interface IError {
  statusCode: number,
  message?: string
}

@Component
export default class ErrorIndex extends Vue {
  @Prop({ type: Object }) error!: IError

  // Data
  show: boolean = true

  // Computed
  get errorTitle (): string {
    if (this.error.statusCode === 404) {
      return 'Not Found'
    }
    return 'Error'
  }

  get errorMessage (): string | undefined {
    // - Debug: show all messages
    if (DEBUG) {
      return this.error.message
    }

    // - Production: filter messages
    if (this.error.statusCode < 500) {
      return this.error.message
    }
  }
}
</script>
