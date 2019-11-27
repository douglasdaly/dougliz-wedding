<template>
  <v-card>
    <!-- Toolbar -->
    <v-toolbar
      :color="color"
      dark
    >
      <!-- Title -->
      <v-btn v-if="syncSelected.length"
        icon
        @click="syncSelected = []"
      >
        <v-icon>mdi-close</v-icon>
      </v-btn>
      <v-toolbar-title>
        {{ syncSelected.length ? `${syncSelected.length} selected` : title }}
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <!-- Actions -->
      <template v-if="showSearch">
        <v-expand-transition>
          <v-text-field v-show="searchVisible"
            ref="searchField"
            v-model="search"
            style="max-width: 200px;"
            label="Search"
            single-line
            hide-details
            @keydown.esc="searchToggle()"
          ></v-text-field>
        </v-expand-transition>
        <v-btn
          icon
          @click="searchToggle()"
        >
          <v-icon v-if="!searchVisible">
            mdi-magnify
          </v-icon>
          <v-icon v-else>
            mdi-close
          </v-icon>
        </v-btn>
      </template>

      <v-btn v-if="bulkExport"
        key="export"
        :disabled="syncSelected.length === 0"
        icon
        @click="$emit('bulk-export')"
      >
        <v-icon>{{ exportIcon }}</v-icon>
      </v-btn>

      <v-btn v-if="bulkDelete"
        key="delete"
        :disabled="syncSelected.length === 0"
        icon
        @click="$emit('bulk-delete')"
      >
        <v-icon>mdi-delete</v-icon>
      </v-btn>

      <slot name="bulk-actions"></slot>
    </v-toolbar>

    <!-- Table -->
    <v-card-text class="py-0">
      <v-row no-gutters>
        <v-col cols="12">
          <v-data-table
            v-model="syncSelected"
            :headers="dispHeaders"
            :items="items"
            :search="search"
            :item-key="itemKey"
            :items-per-page="itemsPerPage"
            :single-select="singleSelect"
            :show-expand="showExpand"
            :single-expand="singleExpand"
            :expanded.sync="expanded"
            :show-select="showSelect"
            calculate-widths
            multi-sort
            @current-items="e => currentItemCount = e.length"
          >
            <!-- Column Filters -->
            <template v-if="showFilterRow" #body.prepend>
              <tr>
                <td></td>
                <td v-for="(header, idx) in dispHeaders"
                  :key="`header-filter-${idx}`"
                >
                  <template v-if="header.filter">
                    <template v-if="header.filterItems">
                      <v-combobox v-if="header.filterSearch"
                        v-model="filters[header.value]"
                        :items="header.filterItems"
                        :label="header.text"
                        :multiple="header.filterMulti"
                        clearable
                        dense
                        single-line
                        hide-details
                      ></v-combobox>
                      <v-select v-else
                        v-model="filters[header.value]"
                        :items="header.filterItems"
                        label="Select"
                        :multiple="header.filterMulti"
                        clearable
                        dense
                        single-line
                        hide-details
                      ></v-select>
                    </template>
                    <v-text-field v-else
                      v-model="filters[header.value]"
                      label="Search"
                      dense
                      single-line
                      hide-details
                    ></v-text-field>
                  </template>
                </td>
              </tr>
            </template>

            <!-- Column Display Adjustments -->
            <template v-for="dispCol in dispFunctions"
              v-slot:[dispCol.name]="{ item }"
            >
              <component :is="dispCol.tag"
                :key="`item-disp-${dispCol.attribute}`"
                v-bind="dispCol.props"
              >
                {{ dispCol.func(item[dispCol.attribute]) }}
              </component>
            </template>

            <!-- Expanded item view -->
            <template v-if="showExpand"
              #expanded-item="{ item, headers }"
            >
              <td :colspan="headers.length">
                <slot :item="item" name="expanded-item"></slot>
              </td>
            </template>

            <!-- Item Actions -->
            <template v-if="hasItemActionSlot" #item.actions="{ item }">
              <slot :item="item" name="item-actions"></slot>
            </template>
          </v-data-table>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import {
  Component,
  Model,
  Prop,
  PropSync,
  Vue,
  Watch
} from 'nuxt-property-decorator'
import { mdiExportVariant } from '@mdi/js'

import { Dict } from '~/types'

import { camelToString } from '~/utils/string'

export interface IHeader {
  value: string
  text?: string
  align?: string
  sortable?: boolean
  width?: string
  display?: (item: any) => any
  displayTag?: string
  displayProps?: object
  filter?: (filterValue: any, value: any) => boolean
  filterItems?: any[]
  filterMulti?: boolean
}

interface IDisplayHeader extends IHeader {
  text: string
  filter?: (value: any) => boolean
  filterItems?: any[]
  filterMulti?: boolean
  filterSearch?: boolean
}

interface ICustomDisplay<T> {
  name: string
  attribute: string
  func: (item: T) => any
  tag: string
  props?: object
}

@Component
export default class SelectTable<T> extends Vue {
  @Model('change', { type: Array }) readonly items!: T[];
  @PropSync('selected', { type: Array }) syncSelected: T[];
  @Prop({ type: String }) title?: string;
  @Prop({ type: Array, default: [] }) headers: (IHeader|string)[];
  @Prop({ type: Boolean, default: true }) showSearch: boolean;
  @Prop({ type: String, default: "uid" }) itemKey: string;
  @Prop({ type: String, default: "primary" }) color: string;
  @Prop({ type: Boolean, default: true }) showSelect: boolean;
  @Prop({ type: Boolean, default: false }) singleSelect: boolean;
  @Prop({ type: Boolean, default: false }) showExpand: boolean;
  @Prop({ type: Boolean, default: false }) singleExpand: boolean;
  @Prop({ type: Number, default: 20 }) itemsPerPage: number;
  @Prop({ type: Boolean, default: true }) bulkExport: boolean;
  @Prop({ type: Boolean, default: true }) bulkDelete: boolean;

  // Data
  $refs!: {
    searchField: HTMLFormElement,
  };

  currentItemCount: number = 0;
  expanded = [];

  search: string = '';
  searchVisible: boolean = false;

  filters: Dict<any> = {};

  // - Icons
  exportIcon: string = mdiExportVariant;

  // Hooks
  created () {
    this.headers.forEach(x => {
      if (typeof x !== 'string' && x.filter) {
        Vue.set(this.filters, x.value, null)
      }
    });
    this.currentItemCount = this.items.length;
  }

  // Watchers
  @Watch('items', { deep: true, immediate: true })
  onItemsChanged(val?: any[], oldVal?: any[]) {
    if (val && oldVal && val.length < oldVal.length) {
      const diff = oldVal.filter(x => !val.includes(x))
      this.syncSelected = this.syncSelected.filter(x => !diff.includes(x))
    }
  }

  // Computed
  get showFilterRow (): boolean {
    if (this.currentItemCount <= 1) {
      return false;
    }
    return Object.keys(this.filters).length > 0;
  }

  get hasItemActionSlot (): boolean {
    return !!this.$scopedSlots['item-actions'];
  }

  get dispHeaders (): IDisplayHeader[] {
    const rv = this.headers.map((x: IHeader|string): IDisplayHeader => {
      if (typeof x === 'string') {
        x = { value: x };
      }
      return {
        ...x,
        text: x.text ? x.text : camelToString(x.value),
        filter: x.filter ? this.getPartial(x.value, x.filter) : undefined,
      };
    });
    if (this.showExpand) {
      rv.push({ text: '', value: 'data-table-expand' });
    }
    if (this.hasItemActionSlot) {
      rv.push({ text: 'Actions', value: 'actions', align: 'center', sortable: false });
    }
    return rv;
  }

  get dispFunctions (): ICustomDisplay<T>[] {
    const rv: ICustomDisplay<T>[] = [];
    this.dispHeaders.forEach(x => {
      if (x.display) {
        rv.push({
          name: `item.${x.value}`,
          attribute: x.value,
          func: x.display,
          tag: x.displayTag || 'span',
          props: x.displayProps,
        });
      }
    });
    return rv;
  }

  // Methods
  getPartial (name: string, func: { (filterValue: any, value: any): boolean }): { (value: any): boolean } {
    return (value: any) => func(this.filters[name], value);
  }

  searchToggle () {
    if (this.search) {
      this.search = '';
    }
    this.searchVisible = !this.searchVisible;
    if (this.searchVisible) {
      this.$nextTick(() => this.$refs.searchField.focus());
    }
  }

}
</script>
