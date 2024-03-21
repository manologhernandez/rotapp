<template>
  <div class="case-container">
    <div><h2>Case Dump</h2></div>
    <div class="case-list border overflow-y-auto px-3 py-3">
      <ol>
        <li v-for="item in props.cases">{{ item }}</li>
      </ol>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  cases: Object,
});
</script>

<style scoped>
.case-list {
  height: 500px;
}
</style>
