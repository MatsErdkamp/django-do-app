<template>
  <div class="graph-container">
    <div v-for="bar in bars" class="bar-item">
      <div
        class="bar-column"

        :style="{ height: bar.height + '%', backgroundColor: bar.color }"
      ></div>
      <div class="bar-text">
        <small v-if="bar.index == 8">now</small>
        <small v-else> &nbsp;</small>
      </div>
    </div>

  </div>

</template>

<script setup>
import { onMounted, ref } from "vue";

const barAmount = 24;
const bars = ref([]);

let previousBarHeight = 50;

onMounted(() => {
  let state = "idle"; // Possible states: "charging", "discharging", "idle"
  let lastHeight = previousBarHeight;

  for (let index = 0; index < barAmount; index++) {
    // Decide whether to switch states based on the current state and some randomness
    switch (state) {
      case "idle":
        // Randomly start charging or discharging from idle
        state = Math.random() < 0.5 ? "charging" : "discharging";
        break;
      case "charging":
        // Switch from charging to idle or discharging based on conditions
        if (lastHeight >= 100) {
          state = "idle"; // Go to idle if fully charged
        } else {
          // Randomly switch to discharging or idle
          state =
            Math.random() < 0.2
              ? "discharging"
              : Math.random() < 0.5
              ? "idle"
              : "charging";
        }
        break;
      case "discharging":
        // Switch from discharging to idle or charging based on conditions
        if (lastHeight <= 0) {
          state = "idle"; // Go to idle if battery is depleted
        } else {
          // Randomly switch to charging or idle
          state =
            Math.random() < 0.2
              ? "charging"
              : Math.random() < 0.5
              ? "idle"
              : "discharging";
        }
        break;
    }

    let hexColor = "#323232";

    // Adjust the height based on the state
    if (state === "charging") {
      lastHeight += 10; // Simulate charging
      hexColor = "#008040";
    } else if (state === "discharging") {
      lastHeight -= 7; // Simulate discharging
      hexColor = "#005090";
    }
    // Idle state does not change the height

    // Ensure battery level stays within bounds
    lastHeight = Math.min(100, Math.max(0, lastHeight));

    // Create a bar representing the current battery level
    let bar = { index: index, height: lastHeight, color: hexColor };
    bars.value.push(bar);
  }
});
</script>

<style scoped>
.graph-container {
  max-width: 100%;

  height: 24svh;
  display: flex;
  align-self: center;

  overflow-x: scroll;
  gap: 4px;
  padding: 12px 4px;
}

.bar-item {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  flex-direction: column;
  max-width: 5vw;
}

.bar-column {
  background: grey;
  min-width: 5vw;
  border-radius: 8px;
}

.bar-text {
  min-height: 20px;

}
</style>
