<template>
  <div>
    <h1>Charge Moments</h1>
    <div class="charge-histogram">
      <div
        class="price-bar"
        v-for="(bar, index) in bars"
        :style="{ height: bar + '%' }"
      ></div>
    </div>

    <div class="charge-histogram-charging-indicator">
      <div
        class="charge-bar"
        :style="indicatorColor(index, deadlineIndex)"
        v-for="(bar, index) in bars"
        @click="clickBar(index)"
      ></div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";

const deadlineIndex = ref(10);
const loading = ref(true);

function indicatorColor(index, compare) {
  if (index == compare) {
    return "background:red;";
  } else if (index > compare) {
    return "background: #212121;";
  } else {
    return "background: #green;";
  }
}

const bars = ref([
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]);

function clickBar(index) {
  deadlineIndex.value = index;
}


async function fetchCalendarData() {
  loading.value = true;
  try {
    const response = await fetch("http://127.0.0.1:8000/api/curve/");
    if (!response.ok) {
      throw new Error("Failed to fetch");
    }
    const data = await response.json();
    bars.value = data;
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  fetchCalendarData();
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
