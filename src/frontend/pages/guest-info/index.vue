<template>
  <v-container class="mb-4">
    <!-- Title -->
    <v-row align="center">
      <v-col align="center" class="pb-0">
        <span class="display-2">
          We can't wait to celebrate with you!
        </span>
      </v-col>
    </v-row>
    <v-row align="center">
      <v-col align="center" class="pt-0">
        <span class="title">
          <i>(We just need to be sure we have your info first)</i>
        </span>
      </v-col>
    </v-row>

    <!-- Form area -->
    <v-row>
      <v-col>
        <v-card>
          <v-card-text>
            <!-- Description -->
            <p>
              Please fill out the form below (we promise we won't share it
              with anyone and your information is stored securely).
            </p>

            <!-- Primary Input -->
            <person-form
              ref="personForm"
              v-model="person"
              :show-titles="true"
              :show-icons="true"
              @submitted="success = true"
            ></person-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, namespace, State, Vue } from 'nuxt-property-decorator'

import PersonForm from '~/components/forms/PersonForm.vue'

import { Person } from '~/types'
import { WeddingSettings } from '~/store/wedding/types'

const nsWedding = namespace('wedding')

@Component({
  components: {
    PersonForm,
  },
  middleware: [
    'guest-auth',
  ]
})
export default class GuestInfo extends Vue {
  @State showLinks!: boolean
  @State siteIsLive!: boolean
  @nsWedding.State settings: WeddingSettings

  // Page meta
  head () {
    return {
      title: 'Guest Information'
    }
  }

  // Data
  success: boolean = false

  person: Person = {
    name: {
      first: '',
      last: ''
    },
    contact: {
      email: '',
      preferredMethod: 'Email'
    },
    address: {
      country: undefined,
      line1: '',
      city: ''
    }
  }
}
</script>
