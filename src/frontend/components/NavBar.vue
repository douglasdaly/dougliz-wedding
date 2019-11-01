<template>
  <v-app-bar
    :app="app"
    :clipped-left="app"
    dense
    :color="color"
  >
    <v-container fluid class="px-0">
      <v-row
        align="center"
        justify="center"
        no-gutters
      >
        <!-- Left title -->
        <v-col
          align="start"
        >
          <v-row
            align="center"
            :class="{ 'ml-1': !showIcon }"
          >
            <v-app-bar-nav-icon
              v-if="showIcon"
              class="mr-1"
              @click.stop="$emit('click')"
            >
              <slot name="navIcon"></slot>
            </v-app-bar-nav-icon>

            <v-toolbar-title>
              <slot name="navTitle">
                Doug & Liz
              </slot>
            </v-toolbar-title>
          </v-row>
        </v-col>

        <!-- Center links -->
        <v-col v-if="$vuetify.breakpoint.mdAndUp"
          cols="auto"
          align="center"
        >
          <v-toolbar-items v-if="mainLinks"
            class="justify-center"
          >
            <nav-links
              :links="mainLinks"
            ></nav-links>
          </v-toolbar-items>
        </v-col>

        <!-- Right -->
        <v-col v-if="$vuetify.breakpoint.smAndUp"
          align="end"
          class="mr-n4 mr-sm-n2"
        >
          <slot name="navRight"></slot>
        </v-col>
      </v-row>
    </v-container>

    <!-- Extension Slot -->
    <template v-if="showPageLinks" v-slot:extension>
      <v-container fluid>
        <v-row align="center" justify="center">
          <v-toolbar-items>
            <nav-links
              :links="pageLinks"
            ></nav-links>
          </v-toolbar-items>
        </v-row>
      </v-container>
    </template>
  </v-app-bar>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'nuxt-property-decorator'

import NavLinks from '~/components/NavLinks.vue'

import { Link } from '~/types'

@Component({
  components: {
    NavLinks
  }
})
export default class NavBar extends Vue {
  @Prop({ type: Boolean, default: false }) showIcon: boolean
  @Prop({ type: Array, required: false }) mainLinks?: Link[]
  @Prop({ type: Array, required: false }) pageLinks?: Link[]
  @Prop({ type: Boolean, default: false }) app: boolean
  @Prop({ type: String, required: false }) color?: string
  @Prop({ type: String, default: 'sm' }) hideBreak: string

  // Computed
  get showPageLinks (): boolean {
    if (!this.pageLinks || this.pageLinks.length === 0) {
      return false
    }
    return true
  }
}
</script>

<style scoped>
.nav-cap {
  width: 20%;
  display: inherit;
  flex-wrap: inherit;
  overflow-x: visible;
}
</style>
