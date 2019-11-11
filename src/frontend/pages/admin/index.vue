<template>
  <v-container fluid class="pt-0">
    <v-row>
      <v-col>
        <h2 class="headline">Site Administration</h2>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component({
  layout: 'admin',
})
export default class AdminIndex extends Vue {

  // Page hooks
  head () {
    return {
      title: 'Admin',
    }
  }

  async fetch ({ store }: any) {
    await Promise.all([
      store.dispatch('admin/clearCrumbs'),
    ])
  }

}
</script>
