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
      dark
      color="primary"
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title>
            {{ userDisplayName }}
          </v-list-item-title>
          <v-list-item-subtitle v-if="userDisplayName !== userEmail">
            {{ userEmail }}
          </v-list-item-subtitle>
        </v-list-item-content>

        <v-btn
          icon
          @click.stop="mini = !mini"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        nav
        dense
      >
        <template v-for="(item, idx) in tools">
          <template v-if="item.name">
            <v-subheader v-if="!mini"
              :key="`${idx}-subheader`"
            >
              {{ item.name }}
            </v-subheader>
            <template v-else>
              <v-divider v-if="idx > 1"
                :key="`${idx}-divider`">
              </v-divider>
            </template>
          </template>
          <v-list-item v-for="(link, lnkIdx) in item.links"
            :key="`${idx}-link-${lnkIdx}`"
            link
          >
            <v-list-item-icon>
              <v-icon>
                {{ link.icon }}
              </v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>
                {{ link.name }}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
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

import { Link, LinkGroup } from '~/types'

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
  @Getter userEmail: string
  @nsAdmin.State toolLinks: LinkGroup[]
  @nsAdmin.State crumbLinks: Link[]

  // Data
  drawer: boolean = true
  mini: boolean = false
  groupIdx = 0

  defaultTools: Link[] = [
    { name: 'Account', url: 'me', icon: 'mdi-account-circle' },
  ]

  toolLinksAdd: LinkGroup[] = [
    {
      links: [
        { name: 'Wedding', url: 'wedding', icon: 'mdi-cards-heart' }
      ],
    },
    {
      name: 'Superuser Tools',
      links: [
        { name: 'Users', url: 'users', icon: 'mdi-account-group' },
        { name: 'Permissions', url: 'permissions', icon: 'mdi-account-lock-outline' },
        { name: 'Settings', url: 'settings', icon: 'mdi-settings-outline' },
      ],
    },
  ]

  // Computed
  get tools (): LinkGroup[] {
    const rv: LinkGroup[] = []

    // - Defaults
    rv.push({ links: this.formatToolLinks(this.defaultTools) })

    // - From state
    for (const toolGrp of this.toolLinksAdd) {
      rv.push({ ...toolGrp, links: this.formatToolLinks(toolGrp.links) })
    }

    return rv
  }

  get crumbs (): Link[] | undefined {
    if (this.crumbLinks && this.crumbLinks.length > 0) {
      return this.crumbLinks
    }
  }

  // Methods
  formatToolLink (link: Link): Link {
    if (link.icon) {
      return link
    }
    return { ...link, icon: `mdi-alpha-${link.name.charAt(0).toLowerCase()}-circle` }
  }

  formatToolLinks (links: Link[]): Link[] {
    return links.map(link => this.formatToolLink(link))
  }
}
</script>
