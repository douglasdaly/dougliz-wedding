<template>
  <div class="pa-0 ma-0">
    <template v-if="oneLine">
      <template v-if="displayTime">
        {{ displayDate }} {{ displayTime }}
      </template>
      <template v-else>
        {{ displayDate }}
      </template>
    </template>
    <ul v-else>
      <li>{{ displayDate }}</li>
      <li>{{ displayTime }}</li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'nuxt-property-decorator'

import { getDisplayDate, getDisplayTime } from '~/utils/display'

@Component
export default class DisplayDatetime extends Vue {
  @Prop(Date) date: Date
  @Prop({ type: Boolean, default: false }) time: boolean
  @Prop(Date) end: Date | undefined
  @Prop({ type: Boolean, default: true }) oneLine: boolean

  // Computed
  get displayDate () {
    return getDisplayDate(this.date, true)
  }

  get displayTime () {
    let rv
    if (this.time)
    {
      if (this.end) {
        rv = `from ${getDisplayTime(this.date, false, false)}`
        rv += ` to ${getDisplayTime(this.end)}`
      } else {
        rv = `at ${getDisplayTime(this.date, false, true)}`
      }
    }
    return rv
  }
}
</script>

<style scoped>
ul {
  list-style-type: none;
}
</style>
