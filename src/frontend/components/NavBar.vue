<template>
  <v-app-bar
    :app="app"
    dense
    :color="color"
  >
    <v-container fluid>
      <v-row
        align="center"
        justify="center"
        no-gutters
      >
        <!-- Left title -->
        <v-col
          align="start"
          class="ml-n4 ml-sm-n2"
        >
          <v-row
            align="center"
            no-gutters
          >
            <v-app-bar-nav-icon v-if="$vuetify.breakpoint.smAndDown"
              class="ml-n2 ml-md-0"
            ></v-app-bar-nav-icon>
            <slot name="navTitle">
              <v-toolbar-title>
                Doug & Liz
              </v-toolbar-title>
            </slot>
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
            <nav-links :links="mainLinks" />
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
    <template v-if="showExtension($vuetify.breakpoint.smAndDown)" v-slot:extension>
      <v-container fluid>
        <v-row align="center" justify="center">
          <v-toolbar-items>
            <nav-links :links="extensionLinks" />
          </v-toolbar-items>
        </v-row>
      </v-container>
    </template>
  </v-app-bar>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'nuxt-property-decorator'

import NavLinks from '~/components/NavLinks.vue'

import { ILink } from '~/types'

@Component({
  components: {
    NavLinks
  }
})
export default class NavBar extends Vue {
  @Prop(Boolean) app: boolean | undefined
  @Prop(Array) mainLinks: ILink[] | undefined
  @Prop(Array) pageLinks: ILink[] | undefined
  @Prop(String) color: string | undefined
  @Prop({ type: String, default: 'sm' }) hideBreak: string

  showExtension (isBreakpoint: boolean): boolean {
    if (this.pageLinks) {
      return true
    } else if (isBreakpoint && this.mainLinks) {
      return true
    }
    return false
  }

  get extensionLinks (): ILink[] | undefined {
    if (this.pageLinks) {
      return this.pageLinks
    }
    return this.mainLinks
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
