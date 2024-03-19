<template>
  <div>
    <h1>Counter: {{ count }}</h1>
    <button @click="increment">Increment</button>
    <button @click="decrement">Decrement</button>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

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
  ws.send(JSON.stringify({ action: 'increment' }));
}

function decrement() {
  ws.send(JSON.stringify({ action: 'decrement' }));
}

onMounted(() => {
  ws.onopen = function() {
    console.log('WebSocket connected.');
  };

  ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    count.value = data.count;
  };

  ws.onerror = function(error) {
    console.log('WebSocket Error: ', error);
  };

  ws.onclose = function(event) {
    console.log('WebSocket closed.');
  };
});

onUnmounted(() => {
  ws.close();
});
</script>