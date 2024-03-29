<template>
  <div class="dashboard-container">
    <DashboardCalendar class="dashboard-item"></DashboardCalendar>
    <DashboardBattery
      class="dashboard-item"
      :charge="batteryPercentage"
      :hours="batteryHours"
    ></DashboardBattery>
    <DashboardHistogram class="dashboard-item"> </DashboardHistogram>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted } from "vue";

import DashboardCalendar from "@/components/DashboardCalendar.vue";
import DashboardBattery from "@/components/DashboardBattery.vue";
import DashboardHistogram from "@/components/DashboardHistogram.vue";

function createWebSocket() {
  // Determine the current web protocol
  var wsProtocol = window.location.protocol === "https:" ? "wss:" : "ws:";

  // Construct the WebSocket URL based on the current domain
  var wsHost = window.location.host; // Includes hostname and port if specified

  if (
    window.location.hostname === "localhost" ||
    window.location.hostname === "127.0.0.1"
  ) {
    wsHost = "localhost:8000";
  }

  var wsPath = "/ws/car/";
  var wsURL = wsProtocol + "//" + wsHost + wsPath;

  return new WebSocket(wsURL);
}

let ws = createWebSocket();

// function increment() {
//   ws.send(JSON.stringify({ action: "increment" }));
// }

// function decrement() {
//   ws.send(JSON.stringify({ action: "decrement" }));
// }

const batteryPercentage = ref(0);
const batteryHours = ref(0);

onMounted(() => {
  ws.onopen = function () {
    console.log("WebSocket connected.");
  };

  ws.onmessage = function (event) {
    const data = JSON.parse(event.data);
    console.log(event.data);

    let batteryResponseCharge = event.data?.car?.battery_percentage;

    if (batteryResponseCharge != undefined) {
      batteryPercentage.value = batteryResponseCharge;
    }

    let batteryResponseHours = event.data?.car?.estimated_time_until_full;

    if (batteryResponseHours != undefined) {
      batteryHours.value = batteryResponseHours;
    }
  };

  ws.onerror = function (error) {
    console.log("WebSocket Error: ", error);
  };

  ws.onclose = function (event) {
    console.log("WebSocket closed.");
  };
});

onUnmounted(() => {
  ws.close();
});
</script>

<style>
.calendar-item {
  border-bottom: 1px solid #212121;
  padding: 4px 16px;
  position: relative;
}

.dashboard-container {
  padding: 32px;
  display: flex;
  gap: 24px;
  flex-direction: row;
}

.dashboard-item {
  border: 1px solid #303030;
  border-radius: 8px;
  background: #121212;
  overflow: hidden;
  height: fit-content;
  max-height: 80vh;
}

.dashboard-item h1 {
  color: white;
  text-transform: uppercase;
  background: #181818;
  border-bottom: 1px solid #212121;
  font-size: 1.2em;
  font-weight: 600;
  padding: 8px 16px;
}
</style>
