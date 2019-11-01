<template>
  <div>
    <template v-for="link in links">
      <v-btn v-if="link.external"
        :key="link.name"
        text
        :href="link.url"
        :target="link.newPage ? 'blank' : undefined"
      >
        {{ link.name }}
      </v-btn>
      <v-btn v-else
        :key="link.name"
        text
        nuxt
        :to="link.url"
        :target="link.newPage ? 'blank' : undefined"
      >
        {{ link.name }}
      </v-btn>
    </template>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'nuxt-property-decorator'

import { Link } from '~/types'

@Component
export default class NavLinks extends Vue {
  @Prop(Array) links!: Link[]
}
</script>
