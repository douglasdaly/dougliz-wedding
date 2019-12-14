<template>
  <v-container fluid class="pt-0">
    <v-row>
      <v-col cols="12" sm="6" md="4">
        <!-- Account info -->
        <v-card
          :loading="loading"
        >
          <v-card-title>
            Login
          </v-card-title>

          <v-card-text v-if="!loading">
            <v-list dense>
              <v-list-item>
                <v-list-item-content>
                  <b class="grey--text text--darken-3">
                    E-mail:
                  </b>
                </v-list-item-content>
                <v-list-item-content class="align-start">
                  {{ user.email }}
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <b class="grey--text text--darken-3">
                    Poweruser?
                  </b>
                </v-list-item-content>
                <v-list-item-content class="align-start">
                  <v-icon v-if="user.isPoweruser"
                    color="success"
                  >
                    mdi-check
                  </v-icon>
                  <v-icon v-else
                    color="error"
                  >
                    mdi-close
                  </v-icon>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <b class="grey--text text--darken-3">
                    Superuser?
                  </b>
                </v-list-item-content>
                <v-list-item-content class="align-start">
                  <v-icon v-if="user.isPoweruser"
                    color="success"
                  >
                    mdi-check
                  </v-icon>
                  <v-icon v-else
                    color="error"
                  >
                    mdi-close
                  </v-icon>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>

          <v-card-actions v-if="!loading">
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              dark
            >
              Reset Password
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>

      <!-- Person Name -->
      <v-col cols="12" sm="6" md="4">
        <v-card
          :loading="loading"
        >
          <v-card-title>
            Name
          </v-card-title>

          <v-card-text v-if="!loading">
            <v-list v-if="user.person && user.person.name"
              dense
            >
              <v-list-item v-if="user.person.name.title">
                <v-list-item-content><b>Title:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.name.title }}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content><b>First:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.name.first }}</v-list-item-content>
              </v-list-item>
              <v-list-item v-if="user.person.name.short">
                <v-list-item-content><b>Short:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.name.short }}</v-list-item-content>
              </v-list-item>
              <v-list-item v-if="user.person.name.middle">
                <v-list-item-content><b>Middle:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.name.middle }}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content><b>Last:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.name.last }}</v-list-item-content>
              </v-list-item>
              <v-list-item v-if="user.person.name.suffix">
                <v-list-item-content><b>Suffix:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.name.suffix }}</v-list-item-content>
              </v-list-item>
            </v-list>
            <p v-else>
              <i>No information.</i>
            </p>
          </v-card-text>

          <v-card-actions v-if="!loading">
            <v-spacer></v-spacer>
            <v-btn v-if="user.person && user.person.name"
              color="primary"
              dark
            >
              Update Name
            </v-btn>
            <v-btn v-else
              color="primary"
              dark
            >
              Add Name
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>

      <!-- Person Contact -->
      <v-col cols="12" sm="6" md="4">
        <v-card
          :loading="loading"
        >
          <v-card-title>
            Contact
          </v-card-title>

          <v-card-text v-if="!loading">
            <v-list v-if="user.person && user.person.contact"
              dense
            >
              <v-list-item v-if="user.person.contact.name">
                <v-list-item-content><b>Name:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.contact.name }}</v-list-item-content>
              </v-list-item>
              <v-list-item v-if="user.person.contact.phone">
                <v-list-item-content><b>Phone:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.contact.phone }}</v-list-item-content>
              </v-list-item>
              <v-list-item v-if="user.person.contact.mobile">
                <v-list-item-content><b>Mobile:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.contact.mobile }}</v-list-item-content>
              </v-list-item>
              <v-list-item v-if="user.person.contact.email">
                <v-list-item-content><b>E-mail:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.contact.email }}</v-list-item-content>
              </v-list-item>
              <v-list-item v-if="user.person.contact.otherValue">
                <v-list-item-content><b>{{ details.contact.otherType }}:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.contact.otherValue }}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content><b>Preferred:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.contact.preferredMethod }}</v-list-item-content>
              </v-list-item>
            </v-list>
            <p v-else>
              <i>No information.</i>
            </p>
          </v-card-text>

          <v-card-actions v-if="!loading">
            <v-spacer></v-spacer>
            <v-btn v-if="user.person && user.person.contact"
              color="primary"
              dark
            >
              Update Contact
            </v-btn>
            <v-btn v-else
              color="primary"
              dark
            >
              Add Contact
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>

      <!-- Person Address -->
      <v-col cols="12" sm="6" md="4">
        <v-card
          :loading="loading"
        >
          <v-card-title>
            Address
          </v-card-title>

          <v-card-text v-if="!loading">
            <v-list v-if="user.person && user.person.address"
              dense
            >
              <v-list-item v-if="user.person.address.name">
                <v-list-item-content><b>Name:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.address.name }}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content><b>Line 1:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.address.line1 }}</v-list-item-content>
              </v-list-item>
              <v-list-item v-if="user.person.address.line2">
                <v-list-item-content><b>Line 2:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.address.line2 }}</v-list-item-content>
              </v-list-item>
              <v-list-item v-if="user.person.address.line3">
                <v-list-item-content><b>Line 3:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.address.line3 }}</v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content><b>City:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.address.city }}</v-list-item-content>
              </v-list-item>
              <v-list-item v-if="user.person.address.state">
                <v-list-item-content><b>State:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.address.state }}</v-list-item-content>
              </v-list-item>
              <v-list-item v-if="user.person.address.zipCode">
                <v-list-item-content><b>Zip Code:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.address.zipCode }}</v-list-item-content>
              </v-list-item>
              <v-list-item v-if="user.person.address.country">
                <v-list-item-content><b>Country:</b></v-list-item-content>
                <v-list-item-content>{{ user.person.address.country }}</v-list-item-content>
              </v-list-item>
            </v-list>
            <p v-else>
              <i>No information.</i>
            </p>
          </v-card-text>

          <v-card-actions v-if="!loading">
            <v-spacer></v-spacer>
            <v-btn v-if="user.person && user.person.address"
              color="primary"
              dark
            >
              Update Address
            </v-btn>
            <v-btn v-else
              color="primary"
              dark
            >
              Add Address
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

import { User } from '~/types'

@Component({
  layout: 'admin',
})
export default class AdminMeIndex extends Vue {
  // Data
  loading: boolean = false;
  user?: User = {
    email: "",
    isActive: true,
    isPoweruser: false,
    isSuperuser: false,
  };

  // Page hooks
  head () {
    return {
      title: 'My Account',
    }
  }

  async mounted () {
    await this.reload();
  }

  async fetch ({ store }: any) {
    await Promise.all([
      store.dispatch('admin/setCrumbs', [
        { name: 'Home', url: '' },
        { name: 'My Account', url: 'me' },
      ]),
    ])
  }

  // Methods
  async reload () {
    this.loading = true;
    this.user = await this.$api.users.getCurrent();
    this.loading = false;
  }

}
</script>
