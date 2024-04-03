<template>
  <div>
    <h1>Battery State</h1>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else>
      <div class="calendar-item">
        <h2>{{ props.charge }}%</h2>
        <div>NOT CONNECTED</div>
        <h2
          style="
            border-top: 1px solid #212121;
            margin-top: 8px;
            padding-top: 4px;
          "
        >
          {{ props.hours }} hours
        </h2>
        <div>For 100% charge</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const batteryData = ref(null);
const loading = ref(false);
const error = ref(null);

const props = defineProps({
  charge: Number,
  hours: Number,
});
</script>

<style scoped>
.error {
  color: red;
}

.calendar-item h2 {
  color: white;
  text-transform: capitalize;
}
</style>
