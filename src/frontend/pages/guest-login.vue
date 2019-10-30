<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-dialog v-model="show"
        persistent
        max-width="600px"
      >
        <v-card hover>
          <v-card-title>
            {{ question }}
          </v-card-title>

          <v-card-text>
            <v-form
              ref="form"
              v-model="valid"
              @submit.prevent="submit"
            >
              <v-text-field
                v-model="answer"
                label="Answer"
                required
                :error-messages="answerErrors"
                @input="$v.answer.$touch()"
                @blur="$v.answer.$touch()"
              ></v-text-field>
            </v-form>
          </v-card-text>

          <v-card-actions>
            <div class="flex-grow-1"></div>
            <v-btn
              :disabled="!valid"
              color="success"
              @click="submit"
            >
              Submit
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>

    <!-- Error snackbar -->
    <v-snackbar
      v-model="incorrect"
      top
      color="error"
    >
      <v-icon>mdi-alert-circle-outline</v-icon>
      <span class="body-1">Incorrect answer</span>
      <v-btn
        text
        @click="incorrect = false"
      >
        Dismiss
      </v-btn>
    </v-snackbar>
  </v-container>
</template>

<script lang="ts">
import { Action, Component, Vue } from 'nuxt-property-decorator'

import { required } from 'vuelidate/lib/validators'

import { checkPasscode, getPasscodePrompt } from '~/api/guest-auth'

@Component
export default class GuestLogin extends Vue {
  @Action('setAllowed') setAllowed: CallableFunction

  // Data
  show: boolean = true
  valid: boolean = false
  question: string = ''
  answer: string = ''
  incorrect: boolean = false
  serverError: string = ''

  async asyncData () {
    const prompt = await getPasscodePrompt()
    return {
      question: prompt
    }
  }

  // Vuelidate
  validations () {
    return {
      answer: {
        required
      }
    }
  }

  get answerErrors () {
    const errors: string[] = []
    if (this.$v.answer) {
      if (!this.$v.answer.$dirty) return errors
      !this.$v.answer.required && errors.push('Answer is required')
    }
    return errors
  }

  // Methods
  async submit () {
    this.$v.$touch()
    if (this.$v.$invalid) {
      return
    }
    const isCorrect = await checkPasscode(this.answer)
    if (isCorrect) {
      this.show = false
      this.setAllowed(true)
      if (this.$route.query.next) {
        this.$router.push(`${this.$route.query.next}`)
      } else {
        this.$router.push("/")
      }
    } else {
      this.$v.$reset()
      this.answer = ''
      this.incorrect = true
    }
  }
}
</script>
