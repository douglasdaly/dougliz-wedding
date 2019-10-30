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
              @click.stop="$emit('click')"
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
            <nav-links
              v-model="mainLinks"
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
            <slot name="pageLinks"></slot>
          </v-toolbar-items>
        </v-row>
      </v-container>
    </template>
  </v-app-bar>
</template>

<script lang="ts">
import { Component, Model, Prop, Vue } from 'nuxt-property-decorator'

import NavLinks from '~/components/NavLinks.vue'

import { Link } from '~/types'

@Component({
  components: {
    NavLinks
  }
})
export default class NavBar extends Vue {
  @Model('change', { type: Array }) mainLinks?: Link[]
  @Prop(Boolean) app?: boolean
  @Prop(String) color?: string
  @Prop({ type: String, default: 'sm' }) hideBreak: string

  // Computed
  get showPageLinks (): boolean {
    if (this.$slots.pageLinks) {
      return true
    }
    return false
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
