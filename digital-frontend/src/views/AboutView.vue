<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>


<script>
var ws = new WebSocket('ws://127.0.0.1:8000/ws/charging/');

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
