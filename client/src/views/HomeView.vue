<script setup>
import { onMounted, ref } from "vue";
import CaseDump from "../components/CaseDump.vue";
import NavBar from "../components/NavBar.vue";

const cases = ref({});

const pullCases = () => {
  fetch("/api/cases/", {
    method: "GET",
  })
    .then((response) => {
      response.json().then((data) => {
        cases.value = data;
      });
    })
    .catch((err) => {
      console.error(err);
    });
};

onMounted(() => {
  pullCases();
});
</script>

<template>
  <main>
    <NavBar />
    <div class="container py-4 px-3 mx-auto">
      <h1>Home view</h1>
      <CaseDump :cases="cases" />
    </div>
  </main>
</template>
