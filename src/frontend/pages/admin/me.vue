<template>
  <v-container fluid class="py-0">
    <v-row>
      <v-col class="pt-0 pl-2">
        <h2 class="headline">My Account</h2>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component({
  layout: 'admin',
})
export default class AdminMeIndex extends Vue {

  // Page hooks
  head () {
    return {
      title: 'My Account',
    }
  }

  async fetch ({ store }: any) {
    await Promise.all([
      store.dispatch('admin/setCrumbs', [
        { name: 'Home', url: '' },
        { name: 'My Account', url: 'me' },
      ]),
    ])
  }

}
</script>
