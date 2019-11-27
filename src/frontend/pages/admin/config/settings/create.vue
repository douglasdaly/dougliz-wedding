<template>
  <v-card>
    <v-card-title
      class="headline"
    >
      New Setting
    </v-card-title>

    <v-card-text>
      <v-form>
        <setting-input
          v-model="setting"
        ></setting-input>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import { Context } from 'vm'
import { Component, Vue } from 'nuxt-property-decorator'

import SettingInput from '~/components/inputs/config/SettingInput.vue'

import { Setting } from '~/types'

@Component({
  components: {
    SettingInput,
  },
  layout: 'admin',
})
export default class AdminConfigSettingsCreate<T> extends Vue {
  // Data
  setting: Setting<T> = {
    name: '',
    required: false,
    value: undefined,
    type: '',
  };

  // Hooks
  head () {
    return {
      title: 'Create Setting',
    };
  }

  async fetch ({ store }: Context) {
    await Promise.all([
      store.dispatch('admin/setCrumbs', [
        { name: 'Home', url: '' },
        { name: 'Config', url: 'config' },
        { name: 'Settings', url: 'config/settings' },
        { name: 'Create', url: 'config/settings/create' },
      ]),
    ]);
  }
}
</script>
