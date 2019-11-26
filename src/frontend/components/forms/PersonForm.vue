<template>
  <v-form v-model="valid">
    <v-container fluid class="py-0">

      <!-- Name -->
      <v-row>
        <v-col>
          <name-input
            ref="nameFields"
            v-model="person.name"
            :title="nameTitle"
            :show-icons="showIcons"
          />
        </v-col>
      </v-row>

      <!-- Addresses -->
      <v-row>
        <v-col>
          <!-- Primary -->
          <address-input
            ref="addressFields"
            v-model="person.address"
            :title="addressTitle"
            :show-icons="showIcons"
          />
        </v-col>
      </v-row>

      <!-- Contact Information -->
      <v-row>
        <v-col>
          <contact-info-input
            ref="contactInfoFields"
            v-model="person.contact"
            :title="contactInfoTitle"
            :show-icons="showIcons"
            :name-prefix="titlePrefix"
          />
        </v-col>
      </v-row>

      <!-- Default Slot -->
      <v-row v-if="hasDefaultSlot">
        <v-col>
          <slot></slot>
        </v-col>
      </v-row>

      <!-- Buttons -->
      <v-row v-if="showButtons">
        <v-col>
          <slot name="buttons">
            <v-btn class="success"
              block
              @click="submitForm()"
            >
              Update
            </v-btn>
          </slot>
        </v-col>
      </v-row>
    </v-container>

    <!-- Error snackbars -->
    <v-snackbar
      v-if="showErrors"
      v-model="sbError"
      color="error"
      top
      multi-line
      :timeout="sbTimeout"
    >
      <v-icon large>mdi-alert</v-icon>
      <div v-if="sbErrorAreas.length > 0"
        class="ma-1"
      >
        <span>Invalid input given for:</span>
        <ul class="ml-1">
          <li v-for="errArea in sbErrorAreas"
            :key="errArea"
          >
            {{ errArea }}
          </li>
        </ul>
      </div>
      <template v-else>
        Invalid input given, please correct the errors below.
      </template>

      <v-btn
        text
        @click="sbError = false"
      >
        Close
      </v-btn>
    </v-snackbar>
  </v-form>
</template>

<script lang="ts">
import { Component, Model, Prop, Vue } from 'nuxt-property-decorator'

import AddressInput from '~/components/inputs/AddressInput.vue'
import ContactInfoInput from '~/components/inputs/ContactInfoInput.vue'
import NameInput from '~/components/inputs/NameInput.vue'

import { Person } from '~/types'

@Component({
  components: {
    NameInput,
    AddressInput,
    ContactInfoInput,
  }
})
export default class PersonForm extends Vue {
  @Model('change', { type: Object }) person!: Person;
  @Prop({ type: Boolean, default: true }) showTitles!: boolean;
  @Prop({ type: Boolean, default: true }) showIcons!: boolean;
  @Prop({ type: Boolean, default: true }) showButtons!: boolean;
  @Prop({ type: Boolean, default: true }) showErrors!: boolean;
  @Prop({ type: String }) titlePrefix?: string;

  $refs: {
    nameFields: NameInput
    contactInfoFields: ContactInfoInput
    addressFields: AddressInput
  }

  // Data
  valid: boolean = false;

  sbError: boolean = false;
  sbErrorAreas: string[] = [];

  // Computed
  get sbTimeout (): number {
    let rv = 6000;
    for (let i=0; i<this.sbErrorAreas.length; i++) {
      rv += 1000;
    }
    return rv;
  }

  get nameTitle (): string | undefined {
    if (this.showTitles) {
      if (this.titlePrefix) {
        return `${this.titlePrefix}'s Name`;
      } else {
        return 'Name';
      }
    }
  }

  get addressTitle (): string | undefined {
    if (this.showTitles) {
      if (this.titlePrefix) {
        return `${this.titlePrefix}'s Address`;
      } else {
        return 'Address';
      }
    }
  }

  get contactInfoTitle (): string | undefined {
    if (this.showTitles) {
      if (this.titlePrefix) {
        return `${this.titlePrefix}'s Contact Information`;
      } else {
        return 'Contact Information';
      }
    }
  }

  get hasDefaultSlot (): boolean {
    return !!this.$slots.default;
  }

  // Methods
  submitForm () {
    if (this.validateForm()) {
      this.valid = true;
      this.$emit('submitted');
    } else {
      this.valid = false;
    }
  }

  validateForm (): boolean {
    this.sbErrorAreas = [];

    const validName = this.$refs.nameFields.formIsValid();
    if (!validName) {
      this.sbErrorAreas.push(this.nameTitle || 'Name');
    }
    const validAddress = this.$refs.addressFields.formIsValid();
    if (!validAddress) {
      this.sbErrorAreas.push(this.addressTitle || 'Address');
    }
    const validContactInfo = this.$refs.contactInfoFields.formIsValid();
    if (!validContactInfo) {
      this.sbErrorAreas.push(this.contactInfoTitle || 'Contact Information');
    }
    const rv = validName && validAddress && validContactInfo;
    this.sbError = !rv;
    return rv;
  }
}
</script>
