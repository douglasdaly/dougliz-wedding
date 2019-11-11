<template>
  <v-container fluid class="fill-width fill-height">
    <v-row align="center" justify="center">
      <v-dialog
        v-model="show"
        max-width="450px"
        persistent
      >
        <v-card>
          <v-toolbar
            dark
            color="primary"
            elevation="1"
          >
            <v-toolbar-title>
              Login
            </v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>

          <v-card-text class="pb-0">
            <v-form
              ref="form"
              v-model="valid"
              @submit.prevent="submit"
              @keyup.enter="submit"
            >
              <v-text-field
                v-model="username"
                label="User"
                required
                prepend-icon="mdi-account"
                :error-messages="usernameErrors"
                @input="$v.username.$touch()"
                @blur="$v.username.$touch()"
                @keyup.enter="submit"
              ></v-text-field>

              <v-text-field
                v-model="password"
                label="Password"
                type="password"
                required
                prepend-icon="mdi-lock"
                :error-messages="passwordErrors"
                @input="$v.password.$touch()"
                @blur="$v.password.$touch()"
                @keyup.enter="submit"
              ></v-text-field>
            </v-form>
          </v-card-text>

          <v-card-actions>
            <div class="flex-grow-1"></div>
            <v-btn
              :disabled="!valid"
              color="primary"
              @click.prevent="submit"
            >
              Login
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
      <span class="body-1">Invalid Login</span>
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

@Component({
  layout: 'default',
})
export default class Login extends Vue {
  @Action userLogin: CallableFunction

  // Data
  valid: boolean = false
  show: boolean = true
  incorrect: boolean = false

  username: string = ''
  password: string = ''

  // Vuelidate
  validations () {
    return {
      username: {
        required
      },
      password: {
        required
      }
    }
  }

  get usernameErrors () {
    const errors: string[] = []
    if (this.$v.username) {
      if (!this.$v.username.$dirty) return errors
      !this.$v.username.required && errors.push('Username is required')
    }
    return errors
  }

  get passwordErrors () {
    const errors: string[] = []
    if (this.$v.password) {
      if (!this.$v.password.$dirty) return errors
      !this.$v.password.required && errors.push('Password is required')
    }
    return errors
  }

  // Methods
  async submit () {
    this.$v.$touch()
    if (this.$v.$invalid) {
      return
    }
    const payload = { username: this.username, password: this.password }
    const result = await this.userLogin(payload)
    if (result) {
      if (this.$route.query.next) {
        this.$router.push({ name: `${this.$route.query.next}` })
      } else {
        this.$router.push({ path: '/' })
      }
    } else {
      this.incorrect = true
    }
  }
}
</script>
