<template>
  <ul class="ma-0 pa-0">
    <li v-for="(line, index) in displayLines"
      :key="index"
    >
      {{ line }}
    </li>
  </ul>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'nuxt-property-decorator'

import { Address } from '~/types'
import { getDisplayAddressLines } from '~/utils/display'

@Component
export default class DisplayAddress extends Vue {
  @Prop(Object) address: Address

  // Computed
  get displayLines (): string[] {
    return getDisplayAddressLines(this.address)
  }
}
</script>

<style scoped>
ul {
  list-style-type: none;
}
</style>
