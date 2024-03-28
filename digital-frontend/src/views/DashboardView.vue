<template>
  <div class="dashboard-container">
    <DashboardCalendar class="dashboard-item"></DashboardCalendar>
    <DashboardBattery class="dashboard-item"></DashboardBattery>
    <DashboardHistogram class="dashboard-item"> </DashboardHistogram>
  </div>
</template>

<script setup>
import DashboardCalendar from "@/components/DashboardCalendar.vue";
import DashboardBattery from "@/components/DashboardBattery.vue";
import DashboardHistogram from "@/components/DashboardHistogram.vue";
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
  background: #212121;
  font-size: 1.2em;
  font-weight: 600;
  padding: 8px 16px;
}
</style>
