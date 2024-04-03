<template>
    <div class="container mt-5">
      <form @submit.prevent="submit()" class="border p-4 bg-light">
        <h2 class="mb-4 text-center">Sign Up!</h2>
  
        <!-- Username Field -->
        <div class="form-group mb-3">
          <label for="usernameInput" class="form-label">Username</label>
          <input type="text" v-model="username" class="form-control" id="usernameInput" placeholder="Enter username" required>
        </div>
  
        <!-- Password Field -->
        <div class="form-group mb-4">
          <label for="passwordInput" class="form-label">Password</label>
          <input type="password" v-model="password" class="form-control" id="passwordInput" placeholder="Password" required>
        </div>

        <div class="form-group mb-4">
          <label for="passwordInput2" class="form-label">Confirm Password</label>
          <input type="password" v-model="password2" class="form-control" id="passwordInput2" placeholder="Password" required>
        </div>
        <div v-if="passwordError" class="alert alert-danger">
            Passwords do not match.
        </div>
        <div v-if="userExistsError" class="alert alert-danger">
            Username already exists.
        </div>
        <!-- Submit Button -->
        <button type="submit" class="btn btn-primary w-100">Submit</button>
      </form>
    </div>
  </template>
  
  
  <script>
      import { defineComponent } from "vue";


      export default defineComponent({
          data() {
              return {
                  username: '',
                  password: '',
                  password2: '',
                  token: '',
                  passwordError: false,
                  userExistsError: false,
              }
          },

      })
  </script>
  
  <style scoped>
  </style>
  