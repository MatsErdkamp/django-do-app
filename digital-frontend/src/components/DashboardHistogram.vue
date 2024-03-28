<template>
  <div>
    <h1>Charge Moments</h1>
    <div class="charge-histogram">
      <div
        class="price-bar"
        v-for="bar in bars"
        :style="{ height: bar + '%' }"
      ></div>
    </div>

    <div class="charge-histogram-charging-indicator">
      <div class="charge-bar" v-for="bar in bars"></div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";

const bars = ref([
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]);

onMounted(() => {
  setTimeout(() => {
    bars.value = [
      20, 40, 60, 70, 80, 100, 20, 30, 20, 40, 60, 70, 80, 100, 20, 30, 20, 40,
      60, 70, 80, 100, 20, 30,
    ];
  }, 200);
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
}

.charge-bar {
  height: 20px;
  background: rgb(38, 231, 61);
  flex: 1;
  border-radius: 8px;
  align-self: flex-end;
}
</style>
