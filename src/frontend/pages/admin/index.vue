<template>
  <v-container fluid class="py-0">
    <v-row>
      <v-col>
        <h1>Admin Site</h1>
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
}
</script>
