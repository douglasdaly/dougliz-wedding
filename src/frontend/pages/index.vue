  <template>
  <section>
    <v-container
      fluid
      class="background-img"
      :style="{'background-image': `url(${require('~/assets/landscape.jpg')})`}"
    >
      <!-- Title image & names -->
      <v-row>
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
      </v-row>

      <!-- Main page content -->
      <v-container>

        <!-- Schedule information -->
        <v-row align="center">
          <v-col>
            <v-card id="schedule"
              class="display-card"
              hover
            >
              <v-card-title class="heading-text">
                Schedule
              </v-card-title>
              <v-card-text>
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
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

        <!-- Travel information -->
        <v-row align="center">
          <v-col>
            <v-card id="travel"
              class="display-card"
              hover
            >
              <v-card-title class="heading-text">
                Travel
              </v-card-title>
              <v-card-text>
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
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

        <!-- Hotels information -->
        <v-row align="center">
          <v-col>
            <v-card id="hotels"
              class="display-card"
              hover
            >
              <v-card-title class="heading-text">
                Hotels
              </v-card-title>
              <v-card-text>
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
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

        <!-- Photos -->
        <v-row align="center">
          <v-col>
            <v-card id="photos"
              class="display-card"
              hover
            >
              <v-card-title class="heading-text">
                Photos
              </v-card-title>
              <v-card-text>
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
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
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
    DisplayDatetime,
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

  // Data
  offsetTop = 0;

  // Hooks
  head () {
    return {
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
        { name: 'Schedule', url: '#schedule' },
        { name: 'Travel', url: '#travel' },
        { name: 'Hotels', url: '#hotels' },
        { name: 'Photos', url: '#photos' },
      ]),
      store.dispatch('setPageLinks'),
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
    if (this.wedding && this.wedding.address) {
      const addrLine = getDisplayAddressLines(this.wedding.address, false).join()
      return `https://maps.google.com/?q=${addrLine}`
    }
  }
}
</script>

<style scoped>
.background-img {
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: center center;
  background-size: cover;
}

.display-card {
  opacity: 0.80;
}

.title-name {
  color: #FFFFFF;
  font-family: 'Charmonman', serif;
  font-size: 60px;
  text-shadow: 1px 2px #424242;
}

.title-seperator {
  color: #FFFFFF;
  font-family: 'Charmonman', serif;
  font-size: 40px;
  font-style: italic;
  text-shadow: 1px 1px #424242;
}
</style>
