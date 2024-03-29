<template>
  <div>
    <h1>Charge Moments</h1>
    <div class="charge-histogram">
      <div
        class="price-bar"
        v-for="(bar, index) in scores"
        :style="{ height: bar + '%' }"
      ></div>
    </div>

    <div class="charge-histogram-charging-indicator">
      <div
        class="charge-bar"
        :style="indicatorColor(bool, index)"
        v-for="(bool, index) in chargeMask"
        @click="clickBar(index)"
      ></div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";

const deadlineIndex = ref(10);
const loading = ref(true);

function indicatorColor(chargeMask, index) {
  if (index == deadlineIndex.value) {
    return "background:orange;";
  }

  if (chargeMask == false) {
    return "background:red;";
  } else {
    return "background:green;";
  }
}

const bars = ref([
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]);

function clickBar(index) {
  deadlineIndex.value = index;
  fetchCurveData();
}

function getURL(endpoint) {

  let host = "https://charging-twin-qw8ag.ondigitalocean.app"

  if (
    window.location.hostname === "localhost" ||
    window.location.hostname === "127.0.0.1"
  ) {
    host = "http://localhost:8000";
  } 

  return host + endpoint;
}

const scores = ref(null);
const chargeMask = ref(null);

async function fetchCurveData() {
  loading.value = true;

  let url = getURL("/api/curve/");

  try {
    const response = await fetch(url + "?deadline=" + deadlineIndex.value);
    if (!response.ok) {
      throw new Error("Failed to fetch");
    }
    const data = await response.json();
    chargeMask.value = data.best_options;
    scores.value = data.scores.split(",").map(function (item) {
      return parseInt(item, 10);
    });
  } catch (err) {
    err.value = err.message;
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  fetchCurveData();
});
</script>

<style>
.charge-histogram,
.charge-histogram-charging-indicator {
  min-width: 400px;
  height: 50vh;
  display: flex;
  flex-direction: row;
  gap: 4px;
  padding: 16px 16px 8px 16px;
}

.charge-histogram-charging-indicator {
  height: unset;
  padding: 0px 16px 16px 16px;
}

.price-bar {
  height: 50%;
  background: rgb(38, 164, 231);
  flex: 1;
  border-radius: 8px;
  align-self: flex-end;
  min-width: 20px;
  transition: all 330ms ease-in-out;
  position: relative;
}

.charge-bar {
  height: 20px;
  background: rgb(26, 167, 42);
  flex: 1;
  border-radius: 8px;
  align-self: flex-end;
  cursor: pointer;
}

.charge-deadline {
  position: absolute;
  background: rgb(191, 24, 127);
  width: 100%;
  top: -32px;
  height: 20px;
  border-radius: 12px;
}
</style>
