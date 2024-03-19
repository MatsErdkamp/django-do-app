<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>


<script>
// Determine the current web protocol
var wsProtocol = window.location.protocol === "https:" ? "wss:" : "ws:";

// Construct the WebSocket URL based on the current domain
var wsHost = window.location.host; // Includes hostname and port if specified

if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
  wsHost = 'localhost:8000'
}

var wsPath = "/ws/charging/";
var wsURL = wsProtocol + "//" + wsHost + wsPath;

var ws = new WebSocket(wsURL);


ws.onmessage = function(e) {
    var data = JSON.parse(e.data);
    console.log(data.message);
};

ws.onopen = function(e) {
    ws.send(JSON.stringify({'message': 'Hello Server!'}));
};


</script>


<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
