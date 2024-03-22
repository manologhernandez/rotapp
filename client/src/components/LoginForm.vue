<template>
  <div>
    <div class="card bg-light" style="border-radius: 1rem">
      <div class="card-body px-5 py-3">
        <div class="my-3">
          <h2 class="fw-bold mb-3 text-uppercase">Login</h2>
          <label class="form-label" for="username-input">Username</label>
          <div class="form-outline form-white mb-4">
            <input
              type="email"
              id="username-input"
              class="form-control"
              v-model="username"
            />
          </div>
          <div class="form-outline form-white mb-4">
            <label class="form-label" for="password-input">Password</label>
            <input
              type="password"
              id="password-input"
              class="form-control"
              v-model="password"
            />
          </div>
          <button class="btn btn-dark px-5" type="submit" @click="login()">
            Login
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const username = ref(null);
const password = ref(null);

function login() {
  console.log("logging in...", username.value, password.value);
  window.location.href = "/";
}
</script>

<style lang="scss" scoped></style>
