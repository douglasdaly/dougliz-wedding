<template>
  <v-app>
    <!-- Navigation bar -->
    <nav-bar
      app
      :title-link="{ name: 'admin' }"
      :page-links="pageLinks"
    >
      <template #navTitle>
        Admin
      </template>

      <template #navRight>
        <v-btn v-if="$vuetify.breakpoint.smAndDown"
          icon
          @click="drawer = !drawer"
        >
          <v-icon>
            mdi-menu
          </v-icon>
        </v-btn>
      </template>
    </nav-bar>

    <!-- Navigation drawer -->
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="showMini"
      app
      right
      dark
      color="secondary"
      clipped
      :hide-overlay="$vuetify.breakpoint.mdAndUp"
      :permanent="$vuetify.breakpoint.mdAndUp"
    >
      <v-list-item>
        <v-list-item-content v-if="!showMini">
          <v-list-item-title>
            {{ userDisplayName }}
          </v-list-item-title>
          <v-list-item-subtitle v-if="userDisplayName !== userEmail">
            {{ userEmail }}
          </v-list-item-subtitle>
        </v-list-item-content>

        <v-btn v-if="$vuetify.breakpoint.mdAndUp"
          icon
          @click.stop="showMini = !showMini"
        >
          <v-icon v-if="!showMini">
            mdi-arrow-collapse-right
          </v-icon>
          <v-icon v-else>
            mdi-backburger
          </v-icon>
        </v-btn>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        nav
      >
        <template v-for="(item, idx) in tools">
          <template v-if="item.name">
            <v-subheader v-if="!mini"
              :key="`${idx}-subheader`"
              class="pl-0"
              style="height: 36px;"
            >
              {{ item.name }}
            </v-subheader>
            <template v-else>
              <v-divider v-if="idx >= 1"
                :key="`${idx}-divider`"
                class="my-2"
              >
              </v-divider>
            </template>
          </template>
          <template v-if="item.main">
            <v-list-group
              :key="`${idx}-main`"
              color="accent"
              :prepend-icon="item.main.icon"
              :group="item.main.url"
            >
              <template #activator>
                <v-list-item-title>
                  {{ item.main.name }}
                </v-list-item-title>
              </template>

              <v-list-item v-for="(link, lnkIdx) in item.links"
                :key="`${idx}-sublink-${lnkIdx}`"
                nuxt
                link
                :to="link.url"
                dense
              >
                <v-list-item-content v-if="!showMini">
                  <v-list-item-title
                    :class="{ 'ml-2': !showMini }"
                  >
                    {{ link.name }}
                  </v-list-item-title>
                </v-list-item-content>

                <v-list-item-icon>
                  <v-icon v-if="showMini"
                    small
                  >
                    mdi-subdirectory-arrow-right
                  </v-icon>
                  <v-icon>
                    {{ link.icon }}
                  </v-icon>
                </v-list-item-icon>
              </v-list-item>
            </v-list-group>
          </template>
          <template v-else>
            <v-list-item v-for="(link, lnkIdx) in item.links"
              :key="`${idx}-link-${lnkIdx}`"
              nuxt
              link
              :to="link.url"
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
              mdi-account-arrow-right
            </v-icon>
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>

    <!-- Main content -->
    <v-content class="main-content">
      <!-- Breadcrumbs -->
      <v-breadcrumbs
        v-if="crumbs"
        :items="crumbs"
        class="px-3 pt-4 pb-0"
      >
        <template #item="props">
          <v-breadcrumbs-item
            nuxt
            exact
            :to="props.item.url"
          >
            {{ props.item.name }}
          </v-breadcrumbs-item>
        </template>
        <template v-slot:divider>
          <v-icon>
            mdi-chevron-right
          </v-icon>
        </template>
      </v-breadcrumbs>

      <!-- Page Content -->
      <v-container fluid class="pa-0">
        <nuxt />
      </v-container>

    </v-content>

    <!-- Application Footer -->
    <footer-bar
      :links="footerLinks"
    ></footer-bar>
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
  drawer: boolean = false
  mini: boolean = false

  // Page hooks
  created () {
    this.drawer = this.$vuetify.breakpoint.mdAndUp
    this.mini = this.$vuetify.breakpoint.mdAndUp
  }

  // Computed
  get showMini (): boolean {
    if (this.$vuetify.breakpoint.smAndDown) {
      return false
    }
    return this.mini
  }
  set showMini (value: boolean) {
    if (this.$vuetify.breakpoint.smAndDown) {
      this.mini = false
    } else {
      this.mini = value
    }
  }

  get tools (): LinkGroup[] {
    const rv: LinkGroup[] = []
    for (const toolGrp of this.toolLinks) {
      rv.push({
        ...toolGrp,
        main: toolGrp.main ? this.formatToolLink(toolGrp.main) : undefined,
        links: this.formatToolLinks(toolGrp.links)
      })
    }
    return rv
  }

  get crumbs (): Link[] | undefined {
    if (this.crumbLinks && this.crumbLinks.length > 0) {
      return this.formatToolLinks(this.crumbLinks)
    }
  }

  get footerLinks (): Link[] | undefined {
    const rv = []
    rv.push({ name: 'Main Site', url: "/" })
    return rv
  }

  // Methods
  formatToolLink (link: Link): Link {
    return {
      ...link,
      url: `/admin/${link.url}`,
      icon: link.icon ? link.icon : `mdi-alpha-${link.name.charAt(0).toLowerCase()}-circle`,
    }
  }

  formatToolLinks (links: Link[]): Link[] {
    return links.map(link => this.formatToolLink(link))
  }
}
</script>
