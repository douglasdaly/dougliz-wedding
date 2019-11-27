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

          <v-col cols="6" sm="auto"
            class="py-0"
          >
            <v-select
              v-model="setting.type"
              :items="typeItems"
              label="Type"
              :error-messages="typeErrors"
              @input="$v.setting.type.$touch()"
              @blur="$v.setting.type.$touch()"
            ></v-select>
          </v-col>

          <v-col cols="6" sm="auto"
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
            <slot name="value-input">
              <component
                :is="valueComponent.tag"
                v-model="setting.value"
                v-bind="valueComponent.props"
                :error-messages="valueErrors"
                @input="$v.setting.value.$touch()"
                @blur="$v.setting.value.$touch()"
              ></component>
            </slot>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Prop, Model, Vue } from 'nuxt-property-decorator'

import { required as vlRequired, requiredIf } from 'vuelidate/lib/validators'

import { Setting } from '~/types'

interface ValueInputComponent {
  tag: string
  props?: object
}

@Component
export default class ConfigSettingInput<T> extends Vue {
  @Model('change', { type: Object }) setting: Setting<T>;
  @Prop({ type: Boolean, default: true }) showIcons: boolean;
  @Prop({ type: String, required: false }) valueInput?: string;

  // Data
  valid: boolean = false;

  typeItems = [
    { text: 'Boolean', value: 4 },
  ]

  // Hooks
  created () {
    this.valid = this.formIsValid(false);
  }

  // Computed
  get valueIsRequired (): boolean {
    if (this.setting.required) {
      return true;
    }
    return false;
  }

  get valueComponent (): ValueInputComponent {
    if (this.valueInput) {
      return { tag: this.valueInput };
    }

    // - Try to determine type
    if (this.setting.type === 4) {
      return {
        tag: 'v-switch',
        props: {
          label: this.setting.value ? 'Enabled' : 'Disabled',
        },
      };
    } else {
      return {
        tag: 'v-text-field',
        props: {
          label: 'Value',
        }
      };
    }
  }

  // Vuelidate
  validations () {
    return {
      setting: {
        name: { vlRequired },
        required: { vlRequired },
        value: {
          required: requiredIf(() => this.valueIsRequired),
        },
        type: { vlRequired },
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
      touch && this.$v.setting.$touch()
      if (!this.$v.setting.$invalid) {
        return true
      }
    }
    return false;
  }

}
</script>
