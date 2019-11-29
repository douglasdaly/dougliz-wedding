<template>
  <v-container fluid class="pa-0">
    <!-- Fields -->
    <v-row>
      <v-col v-if="showIcons"
        cols="auto"
        class="mt-2"
      >
        <v-icon>mdi-settings-box</v-icon>
      </v-col>

      <v-col
        :class="{ 'py-0': true, 'mt-1': showIcons }"
      >
        <v-row>
          <v-col cols="12" sm="6"
            class="py-0"
          >
            <v-text-field
              v-model="setting.name"
              label="Name"
              required
              :error-messages="nameErrors"
              @input="$v.setting.name.$touch()"
              @blur="$v.setting.name.$touch()"
            ></v-text-field>
          </v-col>

          <v-col cols="6" sm="3"
            class="py-0"
          >
            <v-select
              v-model="setting.type"
              :items="allowedTypes"
              label="Type"
              :error-messages="typeErrors"
              @input="$v.setting.type.$touch()"
              @blur="$v.setting.type.$touch()"
            ></v-select>
          </v-col>

          <v-col cols="6" sm="3"
            class="py-0"
          >
            <v-checkbox
              v-model="setting.required"
              label="Required"
              @input="$v.setting.required.$touch()"
              @blur="$v.setting.required.$touch()"
            ></v-checkbox>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12"
            class="py-0"
          >
            <slot :type="setting.type" name="value-input">
              <v-switch v-if="isSwitch"
                v-model="setting.value"
                :label="setting.value ? 'Enabled' : 'Disabled'"
                :error-messages="valueErrors"
                @input="$v.setting.value.$touch()"
                @blur="$v.setting.value.$touch()"
              ></v-switch>
              <v-text-field v-else
                v-model="setting.value"
                label="Value"
                :error-messages="valueErrors"
                @input="$v.setting.value.$touch()"
                @blur="$v.setting.value.$touch()"
              ></v-text-field>
            </slot>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Prop, Model, Vue } from 'nuxt-property-decorator'
import { required, requiredIf } from 'vuelidate/lib/validators'

import { Setting } from '~/types'

import { enumSettingType } from '~/utils/constants'

@Component
export default class SettingInput extends Vue {
  @Model('change', { type: Object }) setting: Setting<any>;
  @Prop({ type: Boolean, default: true }) showIcons: boolean;
  @Prop({ type: String, required: false }) valueInput?: string;

  // Data
  valid: boolean = false;

  // Hooks
  created () {
    this.valid = this.formIsValid(false);
  }

  // Computed
  get isSwitch () {
    return this.setting.type === enumSettingType.BOOLEAN;
  }

  get allowedTypes () {
    return [
      { text: 'Boolean', value: enumSettingType.BOOLEAN },
      { text: 'Datetime', value: enumSettingType.DATETIME },
      { text: 'Float', value: enumSettingType.FLOAT },
      { text: 'Integer', value: enumSettingType.INTEGER },
      { text: 'String', value: enumSettingType.STRING },
      { text: 'UUID', value: enumSettingType.UUID },
    ]
  }

  // Vuelidate
  validations () {
    return {
      setting: {
        name: { required },
        required: { required },
        value: {
          required: requiredIf(() => this.setting.required),
        },
        type: { required },
      },
    };
  }

  get nameErrors (): string[] {
    const errors: string[] = [];
    if (this.$v.setting && this.$v.setting.name) {
      if (!this.$v.setting.name.$dirty) return errors;
      !this.$v.setting.name.required && errors.push("Name is required");
    }
    return errors;
  }

  get valueErrors (): string[] {
    const errors: string[] = [];
    if (this.$v.setting && this.$v.setting.value) {
      if (!this.$v.setting.value.$dirty) return errors;
      !this.$v.setting.value.required && errors.push("Value is required");
    }
    return errors;
  }

  get typeErrors (): string[] {
    const errors: string[] = [];
    if (this.$v.setting && this.$v.setting.type) {
      if (!this.$v.setting.type.$dirty) return errors;
      !this.$v.setting.type.required && errors.push("Type is required");
    }
    return errors;
  }

  // Methods
  formIsValid (touch: boolean = true): boolean {
    if (this.$v.setting) {
      touch && this.$v.setting.$touch();
      if (!this.$v.setting.$invalid) {
        return true;
      }
    }
    return false;
  }

  reset () {
    this.$v.$reset();
  }
}
</script>
