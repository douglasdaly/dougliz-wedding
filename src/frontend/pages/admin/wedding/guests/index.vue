<template>
  <v-container fluid>
    <!-- Test w/ Component -->
    <select-table
      v-model="names"
      :selected.sync="selected"
      title="Wedding Guests"
      :headers="headers"
      item-key="uid"
    >
    </select-table>
  </v-container>
</template>

<script lang="ts">
import { Context } from 'vm'
import { Component, Vue } from 'nuxt-property-decorator'

import { Name } from '~/types'

import SelectTable from '~/components/utils/SelectTable.vue'

@Component({
  components: {
    SelectTable,
  },
  layout: 'admin',
})
export default class AdminWeddingGuestsIndex extends Vue {
  // Data
  names: Name[] = []
  selected: Name[] = []

  // Page hooks
  head () {
    return {
      title: 'Wedding Guests'
    };
  }

  async fetch ({ store }: Context) {
    await Promise.all([
      store.dispatch('admin/setCrumbs', [
        { name: 'Home', url: '' },
        { name: 'Wedding', url: 'wedding' },
        { name: 'Guests', url: 'wedding/guests' },
      ]),
    ])
  }

  async mounted () {
    await this.$api.people.getPeople()
      .then(res => res.forEach(x => this.names.push(x.name)));
  }

  // Computed
  get headers () {
    return [
      'last',
      'first',
    ]
  }
}
</script>
