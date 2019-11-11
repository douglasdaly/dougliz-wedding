<template>
  <v-container fluid class="py-0">
    <v-row>
      <v-col>
        <h1>Configuration</h1>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component({
  layout: 'admin',
})
export default class AdminConfigIndex extends Vue {

  // Page hooks
  head () {
    return {
      title: 'System Admin'
    }
  }

  async fetch ({ store }: any) {
    await Promise.all([
      store.dispatch('admin/addCrumb', { name: 'System', url: 'config' }),
    ])
  }
}
</script>
