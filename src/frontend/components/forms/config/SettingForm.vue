<template>
  <v-card
    :dark="dark"
  >
    <v-card-title v-if="title"
      class="headline"
    >
      {{ title }}
    </v-card-title>

    <v-card-text>
      <v-form
        ref="form"
        v-model="valid"
      >
        <setting-input
          ref="settingInput"
          v-model="setting"
        ></setting-input>
      </v-form>
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn v-if="showCreate"
        color="success"
        @click="submit"
      >
        {{ submitText }}
      </v-btn>
      <v-btn v-if="showClear"
        color="warning"
        @click="reset"
      >
        Clear
      </v-btn>
      <v-btn v-if="showCancel"
        color="error"
        @click="$emit('click:cancel')"
      >
        Cancel
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import { Component, Model, Prop, Vue } from 'nuxt-property-decorator'

import SettingInput from '../../inputs/config/SettingInput.vue'

import { Setting } from '~/types'

@Component({
  components: {
    SettingInput,
  }
})
export default class SettingForm<T> extends Vue {
  @Model('change', { type: Object }) setting: Setting<T>;
  @Prop({ type: String, required: false }) title?: string;
  @Prop({ type: Boolean, default: true }) showCreate: boolean
  @Prop({ type: Boolean, default: true }) showClear: boolean
  @Prop({ type: Boolean, default: false }) showCancel: boolean
  @Prop({ type: Boolean, default: false }) dark?: boolean

  $refs: {
    form: HTMLFormElement
    settingInput: SettingInput
  }

  // Data
  valid: boolean = false;
  update: boolean = false;

  // Computed
  get submitText (): string {
    if (this.setting.uid && this.setting.uid !== '') {
      return 'Update';
    } else {
      return 'Create';
    }
  }

  // Methods
  async submit () {
    this.$emit('click:submit');
    this.valid = this.$refs.settingInput.formIsValid();
    if (this.valid) {
      if (this.setting.uid && this.setting.uid !== '') {
        await this.$api.config.settings.updateSettingId(this.setting.uid, this.setting);
      } else {
        await this.$api.config.settings.createSetting(this.setting);
      }
      this.$emit('submit');
    }
  }

  reset (emitEvent: boolean = true) {
    if (emitEvent) {
      this.$emit('click:reset');
    }
    this.$refs.form.reset();
    this.$refs.settingInput.reset();
  }
}
</script>
