<template>
  <v-container fluid>
    <!-- Test w/ Component -->
    <select-table
      v-model="users"
      :selected.sync="selected"
      title="Users"
      :headers="headers"
    >
    </select-table>
  </v-container>
</template>

<script lang="ts">
import { Context } from 'vm'
import { Component, Vue } from 'nuxt-property-decorator'

import SelectTable from '~/components/inputs/SelectTable.vue'

import { Person, User } from '~/types'

import { getFullName } from '~/utils/display'

@Component({
  components: {
    SelectTable,
  },
  layout: 'admin',
})
export default class AdminConfigUsersIndex extends Vue {
  // Data
  users: User[] = [];
  selected: User[] = [];

  // Hooks
  head () {
    return {
      title: 'Users',
    };
  }

  async fetch ({ store }: Context) {
    await Promise.all([
      store.dispatch('admin/setCrumbs', [
        { name: 'Home', url: '' },
        { name: 'Config', url: 'config' },
        { name: 'Users', url: 'config/users' },
      ]),
    ]);
  }

  async mounted () {
    await this.$api.users.getUsers()
      .then(res => res.forEach(x => this.users.push(x)));
  }

  // Computed
  get headers () {
    return [
      'email',
      {
        value: 'person',
        display: (x: Person) => x && getFullName(x.name),
      },
      {
        value: 'isActive',
        text: 'Is Active?',
        align: 'center',
        display: (x: boolean) => x && 'mdi-check',
        displayTag: 'v-icon',
        displayProps: { small: true },
      },
      {
        value: 'isPoweruser',
        text: 'Is Poweruser?',
        align: 'center',
        display: (x: boolean) => x && 'mdi-check',
        displayTag: 'v-icon',
        displayProps: { small: true },
      },
      {
        value: 'isSuperuser',
        text: 'Is Superuser?',
        align: 'center',
        display: (x: boolean) => x && 'mdi-check',
        displayTag: 'v-icon',
        displayProps: { small: true },
      },
    ];
  }
}
</script>
