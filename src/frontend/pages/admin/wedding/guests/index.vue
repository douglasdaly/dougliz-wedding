<template>
  <v-container fluid class="pt-0">
    <v-row>
      <v-col>
        <select-table
          v-model="names"
          :selected.sync="selected"
          title="Wedding Guests"
          :headers="headers"
          item-key="uid"
        >
        </select-table>
      </v-col>
    </v-row>
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
  loading: boolean = true;
  names: Name[] = [];
  selected: Name[] = [];

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
    await this.reload();
  }

  // Computed
  get headers () {
    return [
      'last',
      'first',
    ]
  }

  // Methods
  async reload () {
    this.loading = true;
    await this.$api.people.getPeople()
      .then(res => res.forEach(x => this.names.push(x.name)));
    this.loading = false;
  }
}
</script>
