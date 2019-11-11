<template>
  <v-footer
    app
    absolute
    padless
    tile
    :color="color"
  >
    <v-container fluid class="pa-0">
      <v-row no-gutters align="center" class="body-2 mx-2">
        <!-- Left side -->
        <v-col v-if="links && links.length > 0"
          cols="auto"
          align="start"
          class="caption"
        >
          <template v-for="(link, index) in links">
            <span
              :key="`${index}-footer-link`"
            >
              <a v-if="link.external"
                :href="link.url"
                :target="link.newPage ? '_blank' : undefined"
                v-text="link.name"
              ></a>
              <nuxt-link v-else
                :to="link.url"
                v-text="link.name"
              ></nuxt-link>
            </span>
            <span v-if="index+1 < links.length && linkSpacer"
              :key="`${index}-footer-link-spacer`"
              class="px-1 caption grey--text"
            >
              {{ linkSpacer }}
            </span>
          </template>
        </v-col>

        <!-- Right side -->
        <v-col align="end" class="caption">
          <slot name="rightSide">
            <span class="grey--text">
              Made with <span class="red--text">❤️</span> by
              <a href="https://github.com/douglasdaly/"
                target="_blank"
                v-text="'Doug'"
              ></a>
            </span>
          </slot>
          <span class="grey--text ml-1">
            &copy; {{ copyYear }}
          </span>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'nuxt-property-decorator'

import { Link } from '~/types'

@Component
export default class FooterBar extends Vue {
  @Prop({ type: String, default: 'secondary' }) color: string
  @Prop(Array) links: Link[] | undefined
  @Prop({ type: String, default: '|', required: false }) linkSpacer?: string

  // Data
  initialYear: number = 2019

  // Computed
  get copyYear (): string {
    const currYear = new Date().getFullYear()
    let rv = `${this.initialYear}`
    if (currYear !== this.initialYear) {
      rv += ` - ${currYear}`
    }
    return rv
  }
}
</script>

<style scoped>
a {
  text-decoration: none;
}
</style>
