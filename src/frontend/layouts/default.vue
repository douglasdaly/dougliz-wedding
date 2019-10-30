<template>
  <v-app>
    <!-- Navigation bar -->
    <nav-bar
      v-model="mainLinks"
      app
      @click="drawer = !drawer"
    >
      <template v-if="displayDate" #navRight>
        <span class="secondary--text">
          {{ displayDate }}
        </span>
      </template>
      <template v-if="pageLinks" #pageLinks>
        <nav-links
          v-model="pageLinks"
        ></nav-links>
      </template>
    </nav-bar>

    <!-- Main content -->
    <v-content class="main-content">
      <!-- Content -->
      <v-container fluid class="pa-0">
        <nuxt />
      </v-container>
    </v-content>

    <!-- Footer -->
    <footer-bar />
  </v-app>
</template>

<script lang="ts">
import {
  Component,
  namespace,
  State,
  Vue
} from 'nuxt-property-decorator'

import FooterBar from '~/components/FooterBar.vue'
import NavBar from '~/components/NavBar.vue'
import NavLinks from '~/components/NavLinks.vue'

import { Link } from '~/types'

import { getDisplayDate } from '~/utils/display'

const nsWedding = namespace('wedding')

@Component({
  components: {
    FooterBar,
    NavBar,
    NavLinks,
  },
  middleware: [
    'clear-links',
  ]
})
export default class Home extends Vue {
  @State isAllowed!: boolean
  @State mainLinks?: Link[]
  @State pageLinks?: Link[]
  @nsWedding.Getter weddingDate?: Date

  // Data
  drawer: boolean = false

  // Computed
  get displayDate (): string | undefined {
    if (this.isAllowed && this.weddingDate) {
      return getDisplayDate(this.weddingDate)
    }
  }
}
</script>

<style scoped>
.main-content {
  background-color: #e0f1d6;
}
</style>
