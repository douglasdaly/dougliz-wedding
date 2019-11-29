<template>
  <v-container fluid class="py-0">
    <!-- Settings Table -->
    <select-table
      v-model="settings"
      :selected.sync="selected"
      title="Settings"
      :headers="headers"
      single-select
    >
      <template #actions>
        <!-- Create -->
        <v-tooltip top>
          <template #activator="{ on }">
            <v-btn
              ref="createButton"
              icon
              :disabled="showForm"
              v-on="on"
              @click="show(true, 'Create Setting')"
            >
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </template>
          <span>Create Setting</span>
        </v-tooltip>

        <!-- Modify -->
        <v-tooltip top>
          <template #activator="{ on }">
            <v-btn icon
              :disabled="!selected.length"
              v-on="on"
              @click="editSelected"
            >
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
          </template>
          <span>Modify Selected</span>
        </v-tooltip>

        <!-- Delete -->
        <v-tooltip top>
          <template #activator="{ on }">
            <v-btn icon
              :disabled="!selected.length"
              v-on="on"
              @click="deleteSelected"
            >
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </template>
          <span>Delete Selected</span>
        </v-tooltip>
      </template>
    </select-table>

    <!-- Create form -->
    <v-dialog v-model="showForm"
      persistent
      max-width="600px"
    >
      <setting-form
        ref="form"
        v-model="setting"
        title="Create Setting"
        show-cancel
        dark
        @submit="show(false)"
        @click:cancel="show(false)"
      ></setting-form>
    </v-dialog>
  </v-container>
</template>

<script lang="ts">
import { Context } from 'vm'
import { Component, Vue } from 'nuxt-property-decorator'

import SettingForm from '~/components/forms/config/SettingForm.vue'
import SelectTable from '~/components/utils/SelectTable.vue'

import { Setting } from '~/types'
import { enumSettingType } from '~/utils/constants'

@Component({
  components: {
    SettingForm,
    SelectTable,
  },
  layout: 'admin',
})
export default class AdminConfigSettingsIndex extends Vue {
  $refs: {
    form: SettingForm<any>,
  };

  // Data
  settings: Setting<any>[] = [];
  selected: Setting<any>[] = [];

  setting: Setting<any> = {
    name: '',
    type: 1,
    required: false,
    value: '',
  };
  showForm: boolean = false;
  isModifying: boolean = false;
  formTitle: string = '';

  loading: boolean = false;

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
    await this.reload();
  }

  // Computed
  get headers () {
    return [
      'name',
      {
        value: 'type',
        text: 'Type',
        display: (x: number) => this.getDisplayType(x),
        displayTag: 'i',
        displayProps: { class: 'grey--text text--darken-1' },
      },
      {
        value: 'required',
        text: 'Required?',
        align: 'center',
        display: (x: boolean) => x ? 'mdi-check' : '',
        displayTag: 'v-icon',
        displayProps: { small: true },
      },
      {
        value: 'value',
        text: 'Value',
        display: (x: any) => typeof x === 'boolean' ? (x ? 'True' : 'False') : x,
      },
    ];
  }

  // Methods
  async reload () {
    this.loading = true;
    this.selected = [];
    this.settings = await this.$api.config.settings.getSettings();
    this.loading = false;
  }

  getDisplayType (value: number): string {
    if (value === enumSettingType.STRING) {
      return 'String';
    } else if (value === enumSettingType.INTEGER) {
      return 'Integer';
    } else if (value === enumSettingType.FLOAT) {
      return 'Float';
    } else if (value === enumSettingType.BOOLEAN) {
      return 'Boolean';
    } else if (value === enumSettingType.DATETIME) {
      return 'Datetime';
    } else if (value === enumSettingType.UUID) {
      return 'UUID';
    } else {
      return 'Unknown';
    }
  }

  show (value: boolean, title?: string) {
    this.showForm = value;
    if (!value) {
      if (this.isModifying) {
        this.setting = {
          name: '',
          type: 1,
          required: false,
          value: '',
        };
        this.isModifying = false;
      }
      this.$refs.form.reset(false);
      this.reload();
    }
    if (title) {
      this.formTitle = title;
    }
  }

  editSelected () {
    this.isModifying = true
    this.setting = { ...this.selected[0] };
    this.show(true, 'Modify Setting');
  }

  async deleteSelected () {
    await Promise.all(this.selected.map((x: Setting<any>) => this.deleteSetting(x.uid)));
    this.selected = [];
  }

  async deleteSetting (id?: string) {
    if (id) {
      await this.$api.config.settings.deleteSettingId(id);
      this.settings = this.settings.filter(x => x.uid !== id);
    }
  }
}
</script>
