<template>
  <v-card
    :dark="dark"
  >
    <v-card-title v-if="title"
      class="headline heading-text"
    >
      {{ title }}
    </v-card-title>

    <v-card-text>
      <v-form
        ref="form"
        v-model="valid"
      >
        <v-container class="py-0">
          <!-- Name -->
          <v-row>
            <v-col class="pt-0">
              <v-text-field
                v-model="event.name"
                label="Name"
                :prepend-icon="showIcons ? 'mdi-party-popper' : undefined"
                :error-messages="nameErrors"
                @input="$v.event.name.$touch()"
                @blur="$v.event.name.$touch()"
              ></v-text-field>
            </v-col>
          </v-row>

          <!-- Dates/Times -->
          <v-row>
            <!-- Date -->
            <v-col cols="12" sm="6" md="4"
              class="pt-0"
            >
              <v-menu
                ref="dateMenu"
                v-model="dateMenu"
                :return-value.sync="displayDate"
                :close-on-content-click="false"
                transition="scale-transition"
                offset-y
                min-width="290px"
              >
                <template #activator="{ on }">
                  <v-text-field
                    v-model="displayDate"
                    label="Date"
                    dense
                    :prepend-icon="showIcons ? 'mdi-calendar' : undefined"
                    :error-messages="dateErrors"
                    readonly
                    @input="$v.date.$touch()"
                    @blur="$v.date.$touch()"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="date"
                  no-title
                  scrollable
                  @click:date="$refs.dateMenu.save(date)"
                ></v-date-picker>
              </v-menu>
            </v-col>

            <!-- Start Time -->
            <v-col cols="12" sm="6" md="4"
              class="pt-0"
            >
              <v-menu
                ref="startMenu"
                v-model="startMenu"
                :return-value.sync="displayStart"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="290px"
                max-width="290px"
              >
                <template #activator="{ on }">
                  <v-text-field
                    v-model="displayStart"
                    label="Start Time"
                    dense
                    :prepend-icon="showIcons ? 'mdi-clock-outline' : undefined"
                    :error-messages="startErrors"
                    readonly
                    @input="$v.event.start.$touch()"
                    @blur="$v.event.start.$touch()"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-time-picker
                  v-if="startMenu"
                  v-model="event.start"
                  ampm-in-title
                  @click:minute="$refs.startMenu.save(event.start)"
                ></v-time-picker>
              </v-menu>
            </v-col>

            <!-- End Time -->
            <v-col v-if="event.start"
              cols="12" sm="6" md="4"
              class="pt-0"
            >
              <v-menu
                ref="endMenu"
                v-model="endMenu"
                :return-value.sync="displayEnd"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="290px"
                max-width="290px"
              >
                <template #activator="{ on }">
                  <v-text-field
                    v-model="displayEnd"
                    label="End Time"
                    dense
                    :prepend-icon="showIcons ? 'mdi-clock-outline' : undefined"
                    :error-messages="endErrors"
                    readonly
                    @input="$v.event.end.$touch()"
                    @blur="$v.event.end.$touch()"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-time-picker
                  v-if="endMenu"
                  v-model="event.end"
                  ampm-in-title
                  :min="event.start"
                  @click:minute="$refs.endMenu.save(event.end)"
                ></v-time-picker>
              </v-menu>
            </v-col>
          </v-row>

          <!-- Address -->
          <v-row>
            <v-col class="pt-0">
              <v-switch
                v-model="showLocation"
                class="py-0 ml-n2"
              >
                <template #label>
                  <span
                    class="ml-2 title"
                    :class="{ 'black--text': showLocation && !dark, 'white--text': showLocation && dark }"
                  >
                    Location
                  </span>
                </template>
              </v-switch>
              <address-input v-if="showLocation"
                ref="locationInput"
                v-model="event.address"
                class="pt-0"
                :show-icons="showIcons"
              />
            </v-col>
          </v-row>

          <!-- Default Slot -->
          <v-row v-if="hasDefaultSlot">
            <v-col>
              <slot></slot>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <!-- Actions -->
      <slot name="actions">
        <v-btn color="success"
          @submit="submit"
        >
          Submit
        </v-btn>
        <v-btn color="warning"
          @click="reset"
        >
          Reset
        </v-btn>
        <v-btn v-if="showCancel"
          color="error"
          @click="$emit('click:cancel')"
        >
          Cancel
        </v-btn>
      </slot>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import { Component, Prop, Model, Vue } from 'nuxt-property-decorator'

import { required } from 'vuelidate/lib/validators'

import AddressInput from '~/components/inputs/AddressInput.vue'

import { Event } from '~/types'

@Component({
  components: {
    AddressInput,
  }
})
export default class EventForm extends Vue {
  @Model('changed', { type: Object }) event: Event;
  @Prop({ type: String, required: false }) title?: string;
  @Prop({ type: Boolean, default: true }) showTitles!: boolean;
  @Prop({ type: Boolean, default: true }) showIcons!: boolean;
  @Prop({ type: Boolean, default: true }) showButtons!: boolean;
  @Prop({ type: Boolean, default: true }) showErrors!: boolean;
  @Prop({ type: Boolean, default: false }) showCancel!: boolean;
  @Prop({ type: Boolean, default: false }) dark: boolean;

  $refs: {
    form: HTMLFormElement
    locationInput: AddressInput
  }

  // Data
  date: string | null = null;

  valid: boolean = false;

  dateMenu: boolean = false;
  startMenu: boolean = false;
  endMenu: boolean = false;

  showLocation: boolean = false;

  // Hooks
  created () {
    if (this.event.date) {
      this.date = this.event.date.toISOString().substr(0, 10);
    }
    if (!this.event.address) {
      this.event.address = { line1: '', city: '' };
    }
    this.valid = this.formIsValid(false);
  }

  // Computed
  get displayDate (): string | null {
    if (this.date) {
      return this.formatDate(this.date);
    }
    return null;
  }

  set displayDate (value: string | null) {
    if (value !== null) {
      this.date = value;
      this.event.date = new Date(value);
    }
  }

  get displayStart (): string | null {
    if (this.event.start) {
      return this.formatTime(this.event.start);
    }
    return null;
  }

  set displayStart (value: string | null) {
    if (value !== null) {
      this.event.start = value;
    }
  }

  get displayEnd (): string | null {
    if (this.event.end) {
      return this.formatTime(this.event.end);
    }
    return null;
  }

  set displayEnd (value: string | null) {
    if (value !== null) {
      this.event.end = value;
    }
  }

  get hasDefaultSlot (): boolean {
    return !!this.$slots.default;
  }

  // Vuelidate
  validations () {
    return {
      event: {
        name: { required },
        start: {},
        end: {},
      },
      date: { required },
    }
  }

  get nameErrors (): string[] {
    const errors: string[] = [];
    if (this.$v.event && this.$v.event.name) {
      if (!this.$v.event.name.$dirty) return errors;
      !this.$v.event.name.required && errors.push("Name is required");
    }
    return errors
  }

  get dateErrors (): string[] {
    const errors: string[] = [];
    if (this.$v.date) {
      if (!this.$v.date.$dirty) return errors;
      !this.$v.date.required && errors.push("Date is required");
    }
    return errors
  }

  get startErrors (): string[] {
    const errors: string[] = [];
    if (this.$v.event && this.$v.event.start) {
      if (!this.$v.event.start.$dirty) return errors;
    }
    return errors;
  }

  get endErrors (): string[] {
    const errors: string[] = [];
    if (this.$v.event && this.$v.event.end) {
      if (!this.$v.event.end.$dirty) return errors;
    }
    return errors;
  }

  // Methods
  formIsValid (touch: boolean = true): boolean {
    if (touch) {
      this.$v.$touch();
    }

    let validAddress;
    if (this.showLocation && !this.$refs.locationInput.formIsValid()) {
      validAddress = true;
    } else {
      validAddress = false;
    }

    return validAddress && !this.$v.$invalid;
  }

  async submit () {
    this.$emit('click:submit');
    this.valid = this.formIsValid();
    if (this.valid) {
      if (this.event.uid && this.event.uid !== '') {
        await this.$api.events.updateEvent(this.event.uid, this.event);
      } else {
        await this.$api.events.createEvent(this.event);
      }
      this.$emit('submit');
    }
  }

  reset (emitEvent: boolean = true) {
    if (emitEvent) {
      this.$emit('click:reset');
    }
    this.$v.$reset();
    if (this.showLocation) {
      this.$refs.locationInput.reset();
      this.showLocation = false;
    }
  }

  // - Date helpers
  formatDate (value: string | null): string | null {
    if (value) {
      const [year, month, day] = value.split('-')
      return `${month}/${day}/${year}`
    }
    return null;
  }

  parseDate (value: string | null): string | null {
    if (value) {
      const [month, day, year] = value.split('/');
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`;
    }
    return null;
  }

  formatTime (value: string | null): string | null {
    if (value) {
      const [hours, mins] = value.split(':').map(x => Number(x));
      const ampm = hours >= 12 ? 'PM' : 'AM';
      const dHours = hours === 12 ? 12 : hours % 12;
      return `${dHours}:${mins.toString().padStart(2, '0')} ${ampm}`;
    }
    return null;
  }
}
</script>
