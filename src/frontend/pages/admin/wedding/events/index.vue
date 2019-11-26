<template>
  <v-card>
    <v-card-title class="headline">
      Events
    </v-card-title>

    <v-card-text>

    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import { Context } from 'vm'
import { Component, Vue } from 'nuxt-property-decorator'

@Component({
  layout: 'admin',
})
export default class AdminWeddingEventsIndex extends Vue {

  // Hooks
  head () {
    return {
      title: "Wedding Events",
    };
  }

  async fetch ({ store }: Context) {
    await Promise.all([
      store.dispatch('admin/setCrumbs', [
        { name: 'Home', url: '' },
        { name: 'Wedding', url: 'wedding' },
        { name: 'Events', url: 'wedding/events' },
      ]),
    ])
  }
}
</script>
