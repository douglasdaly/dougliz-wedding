<template>
  <v-container fluid class="py-0">
    <!-- Settings Table -->
    <select-table
      v-model="settings"
      :selected.sync="selected"
      title="Settings"
      :headers="headers"
    >
    </select-table>
  </v-container>
</template>

<script lang="ts">
import { Context } from 'vm'
import { Component, Vue } from 'nuxt-property-decorator'

import SelectTable from '~/components/utils/SelectTable.vue'

import { Setting } from '~/types'

@Component({
  components: {
    SelectTable,
  },
  layout: 'admin',
})
export default class AdminConfigSettingsIndex extends Vue {
  // Data
  settings: Setting<any>[] = [];
  selected: Setting<any>[] = [];

  // Hooks
  head () {
    return {
      title: 'Settings',
    };
  }

  async fetch ({ store }: Context) {
    await Promise.all([
      store.dispatch('admin/setCrumbs', [
        { name: 'Home', url: '' },
        { name: 'Config', url: 'config' },
        { name: 'Settings', url: 'config/settings' },
      ]),
    ]);
  }

  async mounted () {
    await this.$api.config.settings.getSettings()
      .then(res => res.forEach(x => this.settings.push(x)));
  }

  // Computed
  get headers () {
    return [
      'name',
      {
        value: 'required',
        text: 'Is Required?',
        align: 'center',
        display: (x: boolean) => x && 'mdi-check',
        displayTag: 'v-icon',
        displayProps: { small: true },
      },
      'value',
    ];
  }
}
</script>
