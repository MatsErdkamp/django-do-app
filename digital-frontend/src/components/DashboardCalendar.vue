<template>
  <div>
    <h1>Calendar Data</h1>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else>
      <div v-for="item in calendarData" class="calendar-item">
        <h2>
          {{ item.summary }}
        </h2>
        <div>
          {{ formatDate(item.start.dateTime) }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const calendarData = ref(null);
const loading = ref(false);
const error = ref(null);

// Format the date in a human-readable format using the local timezone
const options = {
  weekday: "long", // "Monday"
  year: "numeric", // "2024"
  month: "long", // "March"
  day: "numeric", // "29"
  hour: "2-digit", // "11"
  minute: "2-digit", // "00"
};

function formatDate(date) {
  const formattedDate = new Intl.DateTimeFormat("en-US", options).format(
    new Date(date)
  );
  return formattedDate;
}

function getURL(endpoint) {

  if (
    window.location.hostname === "localhost" ||
    window.location.hostname === "127.0.0.1"
  ) {
    host = "localhost:8000";
  } else {
    host = ''
  }

  return host + endpoint
}


async function fetchCalendarData() {
  loading.value = true;

  let url = getURL('/api/calendar')

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error("Failed to fetch");
    }
    const data = await response.json();
    calendarData.value = data[0].google_response.items;
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

<style scoped>
.error {
  color: red;
}

.calendar-item:first-child::after {
  content: "CHARGING DEADLINE";
  background: rgb(179, 27, 108);
  position: absolute;
  right: 8px;
  top: 12px;
  padding: 2px 4px;
  border-radius: 8px;
  font-size: 0.8em;
  font-weight: 700;
  color: white;
}

.calendar-item h2 {
  color: white;
  text-transform: capitalize;
}
</style>
