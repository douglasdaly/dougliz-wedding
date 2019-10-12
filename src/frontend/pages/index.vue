  <template>
  <section>
    <!-- Title image & names -->
    <v-container fluid class="pa-0">
      <v-img
        class="white--text align-start"
        src="~/assets/landscape.jpg"
        max-height="500px"
      >
        <div class="d-block text-center mt-4">
          <h2 class="title-name">
            {{ brideNameTitle }}
          </h2>
          <h3 class="title-seperator">
            and
          </h3>
          <h2 class="title-name">
            {{ groomNameTitle }}
          </h2>
        </div>
      </v-img>
    </v-container>

    <!-- Main page content -->
    <v-container>

      <!-- Wedding information -->
      <v-row align="center">
        <v-col align="center">
          <v-card
            hover
          >
            <v-card-title class="justify-center">
              <display-datetime :date="weddingDate" time />
            </v-card-title>

            <v-card-text class="title secondary--text">
              <display-address :address="weddingAddress" />
            </v-card-text>

            <v-card-actions class="justify-center align-center">
              <v-btn
                color="primary"
                target="_blank"
                :href="weddingAddressLink"
              >
                Directions
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>

      <!-- Schedule information -->
      <v-row align="center">
        <v-col align="center">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </p>
        </v-col>
      </v-row>

      <v-row align="center">
        <v-col align="center">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </p>
        </v-col>
      </v-row>

      <v-row align="center">
        <v-col align="center">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </p>
        </v-col>
      </v-row>

    </v-container>
  </section>
</template>

<script lang="ts">
import {
  Component,
  namespace,
  Vue
} from 'nuxt-property-decorator'

import DisplayAddress from '~/components/utils/DisplayAddress.vue'
import DisplayDatetime from '~/components/utils/DisplayDatetime.vue'

import { Address, Name } from '~/types'

import { getFullName, getDisplayAddressLines } from '~/utils/display'

const weddingStore = namespace('wedding')

@Component({
  components: {
    DisplayAddress,
    DisplayDatetime
  },
  middleware: [
    'guest-auth'
  ]
})
export default class Index extends Vue {
  @weddingStore.Getter groomName!: Name
  @weddingStore.Getter brideName!: Name

  // Data
  question: string = ''
  weddingDate: Date = new Date('2020-09-26T15:00:00')
  weddingAddress: Address = {
    name: 'St. Saintly Church',
    line1: '42 Saints Way',
    city: 'Anytown',
    state: 'CT',
    zip: 99999
  }

  // Page meta
  head () {
    return {
      title: 'Wedding',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: 'Doug & Liz\'s Wedding'
        }
      ]
    }
  }

  // Store updates
  async fetch ({ store }: any) {
    await Promise.all([
      store.dispatch('wedding/fetchData')
    ])
  }

  // Computed
  get brideNameTitle () {
    return getFullName(this.brideName)
  }

  get groomNameTitle () {
    return getFullName(this.groomName)
  }

  get weddingAddressLink () {
    const addrLine = getDisplayAddressLines(this.weddingAddress, false).join()
    return `https://maps.google.com/?q=${addrLine}`
  }
}
</script>

<style scoped>
.title-name {
  font-weight: 200;
  font-size: 40px;
  letter-spacing: 1px;
}

.title-seperator {
  font-weight: 50;
  font-size: 20px;
  font-style: italic;
  letter-spacing: 2px;
}
</style>
