<template>
  <v-app>
    <!-- Navigation bar -->
    <nav-bar
      v-model="drawer"
      :page-links="pageLinks"
      app
    >
      <template #navTitle>
        Admin
      </template>
    </nav-bar>

    <!-- Navigation drawer -->
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant.sync="mini"
      app
      clipped
      hide-overlay
      permanent
      color="primary"
      dark
    >
      <v-list-item>
        <v-list-item-title>
          {{ userDisplayName }}
        </v-list-item-title>

        <v-btn
          icon
          @click.stop="mini = !mini"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-list-item>

      <v-divider></v-divider>

      <v-list>
        <v-list-item
          v-for="item in tools"
          :key="item.name"
          link
        >
          <v-list-item-icon>
            <v-icon>
              {{ item.icon }}
            </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>
              {{ item.name }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <template v-slot:append>
        <div class="pa-2">
          <v-btn
            nuxt
            block
          >
            <template v-if="!mini">
              Logout
            </template>
            <v-icon v-else>
              mdi-logout-variant
            </v-icon>
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>

    <!-- Main content -->
    <v-content class="main-content">
      <!-- Breadcrumbs -->
      <v-container v-if="crumbs"
        fluid
        class="pa-0"
      >
        <v-breadcrumbs
          :items="crumbs"
        >
          <template #item="props">
            <v-breadcrumbs-item
              :key="props.item.name"
              nuxt
              :to="props.item.url"
            >
              {{ props.item.name }}
            </v-breadcrumbs-item>
          </template>
        </v-breadcrumbs>
      </v-container>
      <!-- Content -->
      <v-container fluid class="pa-0">
        <nuxt />
      </v-container>
    </v-content>

    <!-- Footer -->
    <footer-bar />
  </v-app>
</template>

<script lang="ts">
import {
  Component,
  Getter,
  namespace,
  State,
  Vue
} from 'nuxt-property-decorator'

import FooterBar from '~/components/FooterBar.vue'
import NavBar from '~/components/NavBar.vue'
import NavLinks from '~/components/NavLinks.vue'

import { Link } from '~/types'

const nsAdmin = namespace('admin')

@Component({
  components: {
    FooterBar,
    NavBar,
    NavLinks,
  },
  middleware: [
    'clear-links',
    'auth',
    'admin-auth'
  ]
})
export default class Home extends Vue {
  @State isAdmin!: boolean
  @State mainLinks: Link[]
  @State pageLinks: Link[]
  @Getter userDisplayName: string
  @nsAdmin.State toolLinks: Link[]
  @nsAdmin.State crumbLinks: Link[]

  // Data
  drawer: boolean = true
  mini: boolean = true

  toolLinksAdd: Link[] = [
    { name: 'Account', url: 'me', icon: 'mdi-account-circle' },
    { name: 'Users', url: 'users', icon: 'mdi-account-group' },
    { name: 'Wedding', url: 'wedding', icon: 'mdi-cards-heart' },
  ]

  // Computed
  get tools (): Link[] {
    return this.toolLinksAdd.map(
      link => link.icon ? link : {...link, icon: `mdi-alpha-${link.name.charAt(0).toLowerCase()}-circle`}
    )
  }

  get crumbs (): Link[] | undefined {
    if (this.crumbLinks && this.crumbLinks.length > 0) {
      return this.crumbLinks
    }
  }
}
</script>
