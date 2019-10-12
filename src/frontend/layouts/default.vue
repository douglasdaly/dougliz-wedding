<template>
  <v-app>
    <!-- Navigation bar -->
    <nav-bar
      :main-links="mainLinks"
      app
    >
      <template v-if="isAllowed" #navRight>
        <span class="secondary--text">
          September 26, 2020
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
    <footer-bar />
  </v-app>
</template>

<script lang="ts">
import { Component, State, Vue } from 'nuxt-property-decorator'

import FooterBar from '~/components/FooterBar.vue'
import NavBar from '~/components/NavBar.vue'

import { ILink } from '~/types'

@Component({
  components: {
    FooterBar,
    NavBar
  }
})
export default class Home extends Vue {
  @State isAllowed!: boolean

  get mainLinks (): ILink[] | undefined {
    if (this.isAllowed) {
      return [
        { external: false, name: 'Home', url: '/' },
        { external: false, name: 'Schedule', url: '#' },
        { external: false, name: 'Travel', url: '#' }
      ]
    }
  }
}
</script>

<style scoped>
.main-content {
  background-color: #d6e7f1;
}
</style>
