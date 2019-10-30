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
          <v-card-text class="pb-0">
            <!-- Description -->
            <p>
              Please fill out the form below (we promise we won't share it
              with anyone and your information is stored securely).
            </p>
            <p class="mb-0">
              If anything should change you can always come back to this same
              link (or bookmark it now) and update any information that needs
              updating: <a href="#link">here</a>
            </p>

            <!-- Input -->
            <person-form
              ref="personForm"
              v-model="person"
              :show-titles="true"
              :show-icons="true"
              :show-buttons="false"
            >
              <template v-if="allowGuestOption">
                <v-switch
                  v-model="includeGuest"
                  :label="`Add ${guestType.toLowerCase()}'s information?`"
                ></v-switch>
              </template>
            </person-form>

            <!-- Guest input -->
            <person-form
              v-if="includeGuest"
              ref="guestForm"
              v-model="guest"
              :show-titles="true"
              :show-icons="true"
              :show-buttons="false"
              :title-prefix="guestType"
            ></person-form>
          </v-card-text>

          <v-card-actions>
            <v-btn
              color="success"
              block
              @click="validateForm()"
            >
              Update
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Context } from 'vm'
import { Component, namespace, Vue } from 'nuxt-property-decorator'

import PersonForm from '~/components/forms/PersonForm.vue'

import { Person } from '~/types'
import { WeddingSettings } from '~/store/wedding/types'

const nsWedding = namespace('wedding')

@Component({
  components: {
    PersonForm,
  }
})
export default class GuestInfoCode extends Vue {
  @nsWedding.State settings: WeddingSettings

  // Page hooks
  head () {
    return {
      title: 'Guest Information'
    }
  }

  async fetch ({ store }: any) {
    await store.dispatch('setAllowed', true)
  }

  validate ({ params }: Context): boolean {
    if (/^[a-z]+$/.test(params.code)) {
      return true
    }
    return false
  }

  // Data
  allowGuestOption: boolean = true
  guestType: string = 'Guest'
  includeGuest: boolean = false

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

  guest: Person = {
    name: {
      first: '',
      last: ''
    },
    contact: {
      email: '',
      preferredMethod: 'Email'
    },
    address: {
      country: '',
      line1: '',
      city: ''
    }
  }

  // Methods
  validateForm () {
    const personValid = (this.$refs.personForm as PersonForm).validateForm()
    let guestValid = true
    if (this.includeGuest) {
      guestValid = (this.$refs.guestForm as PersonForm).validateForm()
    }
    return personValid && guestValid
  }

}
</script>
