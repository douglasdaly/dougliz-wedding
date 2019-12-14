<template>
  <v-container fluid class="pt-0">
    <!-- Events table -->
    <select-table
      v-model="events"
      :selected.sync="selected"
      :loading="loading"
      title="Events"
      :headers="headers"
      item-key="uid"
      @click:add="show(true, 'Create Event')"
      @click:modify="show(true, 'Modify Event')"
    ></select-table>

    <!-- Create form -->
    <v-dialog v-model="showForm"
      persistent
      max-width="600px"
    >
      <event-form
        ref="form"
        v-model="newEvent"
        :title="formTitle"
        show-cancel
        dark
        @submit="show(false)"
        @click:cancel="show(false)"
      >
      </event-form>
    </v-dialog>
  </v-container>
</template>

<script lang="ts">
import { Context } from 'vm'
import { Component, Vue } from 'nuxt-property-decorator'

import { Event } from '~/types'

import EventForm from '~/components/forms/EventForm.vue'
import SelectTable from '~/components/utils/SelectTable.vue'

@Component({
  components: {
    EventForm,
    SelectTable,
  },
  layout: 'admin',
})
export default class AdminWeddingEventsIndex extends Vue {
  $refs: {
    form: EventForm
  };

  // Data
  loading: boolean = true;
  events: Event[] = [];
  selected: Event[] = [];

  showForm: boolean = false;
  formTitle: string = 'Create Event';
  isModifying: boolean = false;
  newEvent: Event = {
    name: '',
    date: new Date(),
  }

  // Hooks
  head () {
    return {
      title: "Wedding Events",
    };
  }

  async fetch ({ store }: Context) {
    await Promise.all([
      store.dispatch('admin/setCrumbs', [
        { name: 'Home', url: '' },
        { name: 'Wedding', url: 'wedding' },
        { name: 'Events', url: 'wedding/events' },
      ]),
    ])
  }

  async mounted () {
    await this.reload();
  }

  // Computed
  get headers () {
    return [
      'date',
      'name',
      'start',
      'end',
      'address',
    ];
  }

  // Methods
  async reload () {
    this.loading = true;
    this.selected = [];
    this.events = await this.$api.events.getAllEvents();
    this.loading = false;
  }

  show (value: boolean, title?: string) {
    this.showForm = value;
    if (!value) {
      if (this.isModifying) {
        this.newEvent = {
          name: '',
          date: new Date(),
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
    this.newEvent = { ...this.selected[0] };
    this.show(true, 'Modify Event');
  }

  async deleteSelected () {
    await Promise.all(this.selected.map((x: Event) => this.deleteEvent(x.uid)));
    this.selected = [];
  }

  async deleteEvent (id?: string) {
    if (id) {
      await this.$api.events.deleteEvent(id);
      this.events = this.events.filter(x => x.uid !== id);
    }
  }
}
</script>
