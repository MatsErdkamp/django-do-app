<template>
  <div class="dashboard-container">
    <DashboardCalendar class="dashboard-item"></DashboardCalendar>
  </div>
</template>

<script setup>
import DashboardCalendar from "@/components/DashboardCalendar.vue";
</script>

<style>
.dashboard-container {
  padding: 32px;
}

.dashboard-item {
  border: 1px solid #303030;
  border-radius: 8px;
  background: #121212;
  overflow: hidden;
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
