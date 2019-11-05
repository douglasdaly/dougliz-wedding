  <template>
  <section>
    <!-- Title image & names -->
    <v-container fluid class="pa-0">
      <v-img
        class="white--text align-center"
        src="~/assets/landscape.jpg"
        max-height="500px"
      >
        <v-col align="center">
          <v-row justify="center">
            <h2 class="title-name">
              {{ brideNameTitle }}
            </h2>
          </v-row>
          <v-row justify="center">
            <h3 class="title-seperator">
              and
            </h3>
          </v-row>
          <v-row justify="center">
            <h2 class="title-name">
              {{ groomNameTitle }}
            </h2>
          </v-row>
        </v-col>
      </v-img>
    </v-container>

    <!-- Main page content -->
    <v-container>

      <!-- Wedding information -->
      <v-row align="center">
        <v-col align="center">
          <v-card
            v-if="wedding"
            hover
            max-width="550"
          >
            <v-card-title
              v-if="wedding.date"
              class="justify-center"
            >
              <display-datetime
                :date="wedding.date"
                time
              ></display-datetime>
            </v-card-title>

            <v-card-text
              class="title secondary--text"
            >
              <display-address
                v-if="wedding.address"
                :address="wedding.address"
              ></display-address>
            </v-card-text>

            <v-card-actions
              class="justify-center align-center"
            >
              <v-btn
                v-if="wedding.address"
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
        <v-col id="schedule">
          <h2>
            Schedule
          </h2>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </p>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </p>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </p>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </p>
        </v-col>
      </v-row>

      <!-- Travel information -->
      <v-row align="center">
        <v-col id="travel">
          <h2>
            Travel
          </h2>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </p>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </p>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </p>
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
  Action,
  Component,
  namespace,
  Vue
} from 'nuxt-property-decorator'

import DisplayAddress from '~/components/utils/DisplayAddress.vue'
import DisplayDatetime from '~/components/utils/DisplayDatetime.vue'

import { Event, Name } from '~/types'

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
  @Action setMainLinks: CallableFunction
  @weddingStore.Getter groomName!: Name
  @weddingStore.Getter brideName!: Name
  @weddingStore.State wedding?: Event

  // Page hooks
  head () {
    return {
      title: 'Wedding',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: 'Doug & Liz\'s Wedding Website'
        }
      ]
    }
  }

  async fetch ({ store }: any) {
    await Promise.all([
      store.dispatch('setMainLinks', [
        { name: 'Home', url: '/' },
        { name: 'Schedule', url: '#schedule' },
        { name: 'Travel', url: '#travel' },
      ]),
      store.dispatch('setPageLinks'),
      store.dispatch('wedding/fetchData')
    ])
  }

  // Data
  question: string = ''

  // Computed
  get brideNameTitle () {
    return getFullName(this.brideName)
  }

  get groomNameTitle () {
    return getFullName(this.groomName)
  }

  get weddingAddressLink () {
    if (this.wedding && this.wedding.address) {
      const addrLine = getDisplayAddressLines(this.wedding.address, false).join()
      return `https://maps.google.com/?q=${addrLine}`
    }
  }
}
</script>

<style scoped>
.title-name {
  font-family: 'Tangerine', serif;
  font-size: 80px;
  letter-spacing: 6px;
  text-shadow: 1px 2px #424242;
}

.title-seperator {
  font-family: 'Tangerine', serif;
  font-size: 50px;
  font-style: italic;
  letter-spacing: 4px;
  text-shadow: 1px 1px #424242;
}
</style>
