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
            <p class="mb-0">
              Please fill out the form below (we promise we won't share it
              with anyone and your information is stored securely).  If
              anything should change you can always come back to this same
              link and update anything that needs updating.
            </p>

            <!-- Input areas -->
            <v-form v-model="valid">
              <v-container fluid class="py-0">

                <!-- Name(s) -->
                <v-row>
                  <v-col>
                    <!-- Primary -->
                    <name-input
                      v-model="person.name"
                      title="Name"
                    />
                  </v-col>
                </v-row>

                <!-- Guest (w/o optionality) -->
                <v-row v-if="!allowGuestOption && includeGuest">
                  <v-col>
                    <name-input
                      v-model="guest.name"
                      :title="`${guestType}'s Name`"
                    />
                  </v-col>
                </v-row>

                <!-- Guest (w/ optionality) -->
                <v-row v-if="allowGuestOption">
                  <v-col cols="auto"
                    class="py-0"
                  >
                    <v-icon v-if="!includeGuest"
                      color="success"
                    >
                      mdi-account-multiple-plus
                    </v-icon>
                    <v-icon v-else>
                      mdi-account-multiple
                    </v-icon>
                  </v-col>
                  <v-col class="py-0">
                    <v-row>
                      <v-col class="py-0">
                        <!-- Add/remove guest -->
                        <v-switch
                          v-model="includeGuest"
                          class="pa-0 ma-0"
                          :hide-details="true"
                        >
                          <template v-if="!includeGuest" #label>
                            <span class="success--text">Add {{ guestType }}</span>
                          </template>
                          <template v-else #label>
                            <span class="error--text">Remove {{ guestType }}</span>
                          </template>
                        </v-switch>
                      </v-col>
                    </v-row>
                    <v-row v-if="includeGuest">
                      <v-col class="pb-0">
                        <!-- Guest's name -->
                        <name-input v-if="includeGuest"
                          v-model="guest.name"
                          :title="`${guestType}'s Name`"
                          :show-icons="false"
                        />
                      </v-col>
                    </v-row>
                  </v-col>
                </v-row>

                <!-- Contact Information -->
                <v-row>
                  <v-col>
                    <!-- Primary -->
                    <contact-info-input
                      v-model="person.contact"
                      title="Contact Information"
                    />
                  </v-col>
                </v-row>
                <v-row v-if="includeGuest">
                  <v-col cols="auto"
                    class="py-0"
                  >
                    <v-icon v-if="!includeGuestContact"
                      color="success"
                    >
                      mdi-account-multiple-plus-outline
                    </v-icon>
                    <v-icon v-else>
                      mdi-account-multiple-outline
                    </v-icon>
                  </v-col>
                  <v-col class="py-0">
                    <v-row>
                      <v-col class="py-0">
                        <v-switch
                          v-model="includeGuestContact"
                          class="pa-0 ma-0"
                          :hide-details="true"
                        >
                          <template v-if="!includeGuestContact" #label>
                            <span class="success--text">Add {{ guestType }}'s</span>
                          </template>
                          <template v-else #label>
                            <span class="error--text">Remove {{ guestType }}'s</span>
                          </template>
                        </v-switch>
                      </v-col>
                    </v-row>
                    <v-row v-if="includeGuestContact">
                      <v-col>
                        <contact-info-input
                          v-model="guest.contact"
                          :title="`${guestType}'s Contact Information`"
                          :show-icons="false"
                        />
                      </v-col>
                    </v-row>
                  </v-col>
                </v-row>

                <!-- Addresses -->
                <v-row>
                  <v-col>
                    <!-- Primary -->
                    <address-input
                      v-model="person.address"
                      title="Address"
                    />
                  </v-col>
                </v-row>
              </v-container>
            </v-form>
          </v-card-text>

          <!-- Buttons -->
          <v-card-actions>
            <v-btn class="success">
              Update
            </v-btn>
            <v-btn class="error">
              Clear
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

import AddressInput from '~/components/inputs/AddressInput.vue'
import ContactInfoInput from '~/components/inputs/ContactInfoInput.vue'
import NameInput from '~/components/inputs/NameInput.vue'

import { Person } from '~/types'

@Component({
  components: {
    AddressInput,
    ContactInfoInput,
    NameInput
  }
})
export default class GuestInfo extends Vue {
  // Page meta
  head () {
    return {
      title: 'Guest Information'
    }
  }

  // Data
  valid: boolean = true

  allowGuestOption: boolean = true
  guestType: string = 'Guest'
  includeGuest: boolean = false
  includeGuestContact: boolean = false

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
      line1: '',
      city: ''
    }
  }
}
</script>
