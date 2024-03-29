<template>
  <div>
    <div class="counter-number">
      <Transition :key="count" name="fade">
        <h1>{{ count }}</h1>
      </Transition>
    </div>
    <div class="counter-buttons">
      <button @click="increment">Increment</button>
      <button @click="decrement">Decrement</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const count = ref(0);

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

  var wsPath = "/ws/counter/";
  var wsURL = wsProtocol + "//" + wsHost + wsPath;

  return new WebSocket(wsURL);
}

let ws = createWebSocket();

function increment() {
  ws.send(JSON.stringify({ action: "increment" }));
}

function decrement() {
  ws.send(JSON.stringify({ action: "decrement" }));
}

onMounted(() => {
  ws.onopen = function () {
    console.log("WebSocket connected.");
  };

  ws.onmessage = function (event) {
    const data = JSON.parse(event.data);
    console.log(event.data)

    count.value = data.count;
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

<style scoped>
.counter-number {
  font-size: 10em;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  height: 60vh;
  color: rgb(12, 104, 190);
  text-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
  font-weight: 700;
  font-family: monospace;
}

.counter-buttons {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
}


/* we will explain what these classes do next! */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

</style>
