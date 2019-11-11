<template>
  <v-app>
    <!-- Navigation bar -->
    <nav-bar
      app
      :main-links="mainLinks"
      :page-links="pageLinks"
    >
      <template v-if="displayDate" #navRight>
        <span class="secondary--text">
          {{ displayDate }}
        </span>
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
    <footer-bar
      :links="footerLinks"
    ></footer-bar>
  </v-app>
</template>

<script lang="ts">
import {
  Component,
  Getter,
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
  @Getter isAdmin!: boolean
  @State mainLinks: Link[]
  @State pageLinks: Link[]
  @nsWedding.Getter weddingDate?: Date

  // Computed
  get displayDate (): string | undefined {
    if (this.isAllowed && this.weddingDate) {
      return getDisplayDate(this.weddingDate)
    }
  }

  get footerLinks (): Link[] | undefined {
    const rv = []
    if (this.isAdmin) {
      rv.push({ name: 'Admin', url: '/admin' })
    }
    return rv
  }
}
</script>
