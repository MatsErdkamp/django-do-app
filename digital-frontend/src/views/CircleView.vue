<template>
  <div class="circle-container">
    <div id="chartdiv"></div>

    <div class="rotating-dial"></div>
    <div class="rotating-dial-2"></div>

    <div class="circle-inside">
      <div class="clock">{{ new Date().toLocaleTimeString() }}</div>

      <div class="deadline-clock">{{ chargeDeadline }}</div>
      <div class="charge-deadline">charge deadline for 'work'</div>

      <Transition mode="out-in" name="fade">
        <div class="charge-indicator" v-if="carState != 'plugged_in'" style="background: #c71d3b" >Car not plugged in</div>
        <div class="charge-indicator" v-else-if="charging == true">Charging 54%</div>
        <div class="charge-indicator" v-else style="background: #e49623" >
          Not Charging 54%
        </div>
      </Transition>
    </div>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from "vue";

// Reactive value for chargeDeadline

const chargeDeadline = ref("14:00");
const rotation = ref(0); // Initial rotation in degrees



const charging = ref(false);
const carState = ref('Not Connected');


onMounted(() => {
  fetchCurveData();
  createChart();
  handleRotation();
});

let series;
let series2;
let chargeData = [];

const scores = ref([]);

function createChart() {
  am5.ready(function () {
    // Create root element
    // https://www.amcharts.com/docs/v5/getting-started/#Root_element
    var root = am5.Root.new("chartdiv");

    // Set themes
    // https://www.amcharts.com/docs/v5/concepts/themes/
    root.setThemes([am5themes_Animated.new(root)]);

    // Create chart
    // https://www.amcharts.com/docs/v5/charts/xy-chart/
    var chart = root.container.children.push(
      am5radar.RadarChart.new(root, {
        panX: false,
        panY: false,
        wheelX: "none",
        wheelY: "none",
        startAngle: -84,
        endAngle: 264,
        innerRadius: am5.percent(75),
      })
    );

    // Create axes
    // https://www.amcharts.com/docs/v5/charts/xy-chart/axes/
    var xRenderer = am5radar.AxisRendererCircular.new(root, {
      minGridDistance: 30,
    });

    xRenderer.grid.template.set("forceHidden", true);
    // Change X-axis label color to white
    xRenderer.labels.template.set("fill", am5.color(0xffffff));

    var xAxis = chart.xAxes.push(
      am5xy.CategoryAxis.new(root, {
        maxDeviation: 0,
        categoryField: "category",
        renderer: xRenderer,
      })
    );

    var yRenderer = am5radar.AxisRendererRadial.new(root, {});
    yRenderer.labels.template.set("centerX", am5.p50);
    // Change X-axis label color to white
    yRenderer.labels.template.set("fill", am5.color(0xffffff));

    var yAxis = chart.yAxes.push(
      am5xy.ValueAxis.new(root, {
        maxDeviation: 0.3,
        min: 0,
        max: 110,
        renderer: yRenderer,
      })
    );

    // Add series
    // https://www.amcharts.com/docs/v5/charts/xy-chart/series/
    series = chart.series.push(
      am5radar.RadarColumnSeries.new(root, {
        name: "Series 1",
        sequencedInterpolation: true,
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "value",
        categoryXField: "category",
        stacked: true,
      })
    );

    // Rounded corners for columns
    series.columns.template.setAll({
      cornerRadius: 5,
      tooltipText: "{categoryX}: {valueY}",
    });

    for (var i = 0; i < 24; i++) {
      chargeData.push({ category: i, value: 20 });
    }

    chargeData.forEach((item, index) => {
      item.colorState = chargeMask[index] === true ? "#22e66a" : "#212121";
    });

    series.columns.template.adapters.add("fill", (fill, target) => {
      return target.dataItem.dataContext.colorState;
    });

    series.columns.template.adapters.add("stroke", (stroke, target) => {
      return target.dataItem.dataContext.colorState;
    });

    // Add series
    // https://www.amcharts.com/docs/v5/charts/xy-chart/series/
    series2 = chart.series.push(
      am5radar.RadarColumnSeries.new(root, {
        name: "Series 1",
        sequencedInterpolation: true,
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "value",
        categoryXField: "category",
        stacked: true,
      })
    );

    // Rounded corners for columns
    series2.columns.template.setAll({
      cornerRadius: 5,
      tooltipText: "{categoryX}: {valueY}",
    });

    series2.columns.template.adapters.add("fill", function (fill, target) {
      return "#2263e6";
    });

    series2.columns.template.adapters.add("stroke", function (stroke, target) {
      return "#2263e6";
    });

    xAxis.data.setAll(chargeData);
    series.data.setAll(chargeData);

    setData(
      series2,
      [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0,
      ]
    );

    // Make stuff animate on load
    // https://www.amcharts.com/docs/v5/concepts/animations/
    series.appear(1000);
    series2.appear(1000);
    chart.appear(1000, 100);
  });
}

function setData(series, data) {
  // Set data
  var data2 = [];

  for (var i = 0; i < 24; i++) {
    data2.push({ category: i, value: data[i] });
  }

  series.data.setAll(data2);
}

// Element reference for rotating dial
const rotatingDial = ref(null);

function handleRotation() {
  rotatingDial.value = document.querySelector(".rotating-dial");

  // Mouse movement handling
  let isDragging = false;
  let startAngle = 0;

  const startRotation = (event) => {
    // Prevent default action for the event to avoid potential scrolling or other touch actions
    event.preventDefault();

    isDragging = true;
    const rect = rotatingDial.value.getBoundingClientRect();
    let clientX = event.clientX;
    let clientY = event.clientY;

    // Handle touch start
    if (event.touches) {
      clientX = event.touches[0].clientX;
      clientY = event.touches[0].clientY;
    }

    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    startAngle = Math.atan2(clientY - centerY, clientX - centerX);

    // Add both mouse and touch move/end listeners
    document.addEventListener("mousemove", rotateDial);
    document.addEventListener("mouseup", stopRotation);
    document.addEventListener("touchmove", rotateDial, { passive: false }); // Use passive: false to allow preventDefault
    document.addEventListener("touchend", stopRotation);
  };

  rotatingDial.value.addEventListener("mousedown", startRotation);
  rotatingDial.value.addEventListener("touchstart", startRotation, {
    passive: false,
  });

  const rotateDial = (event) => {
    event.preventDefault();

    if (!isDragging) return;

    const rect = rotatingDial.value.getBoundingClientRect();
    let clientX = event.clientX;
    let clientY = event.clientY;

    // Handle touch move
    if (event.touches) {
      clientX = event.touches[0].clientX;
      clientY = event.touches[0].clientY;
    }

    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    const currentAngle = Math.atan2(clientY - centerY, clientX - centerX);
    const deltaAngle = currentAngle - startAngle;
    rotation.value += deltaAngle * (180 / Math.PI);
    rotatingDial.value.style.transform = `rotate(${rotation.value}deg)`;

    let val = rotation.value;

    if (val < 0) {
      val = 360 + val;
    }

    // Simplified update of chargeDeadline based on rotation
    // You may want to adjust this calculation
    let currentTime = new Date().getHours();

    let hours = Math.floor((val % 350) / 14.5) + currentTime;

    if (hours >= 24) {
      hours -= 24;
    }

    chargeDeadline.value = `${hours}:00`;

    deadlineOffset = hours - currentTime;

    if (deadlineOffset < 0) {
      deadlineOffset += 24;
    }

    startAngle = currentAngle;

    debounceFetchCurveData();
  };

  const stopRotation = () => {
    isDragging = false;
    document.removeEventListener("mousemove", rotateDial);
    document.removeEventListener("mouseup", stopRotation);
    document.removeEventListener("touchmove", rotateDial);
    document.removeEventListener("touchend", stopRotation);
  };
}

// Define a debounced version of fetchCurveData
let debounceTimer;
function debounceFetchCurveData() {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => {
    fetchCurveData();
  }, 100); // Debounce time of 200ms
}

let deadlineOffset = 5;

const loading = ref(true);
async function fetchCurveData() {
  loading.value = true;

  let url = getURL("/api/curve/");

  try {
    const response = await fetch(
      url + "?deadline=" + deadlineOffset + "&hours=" + 10
    );
    if (!response.ok) {
      throw new Error("Failed to fetch");
    }
    const data = await response.json();
    chargeMask = data.best_options;

    scores.value = data.scores.split(",").map(function (item) {
      return parseInt(item, 10);
    });

    setData(series2, scores.value);

    // Assuming your data update logic happens here
    chargeMask.forEach((isActive, index) => {
      chargeData[index].colorState = isActive ? "#22e66a" : "#212121";
    });

    if (chargeMask[0] == true) {
      charging.value = true;
    } else {
      charging.value = false;
    }

    // Call this function whenever you need to update the chart's color states
    updateColorStatesAndRefreshData(series, chargeData);
  } catch (err) {
    console.log(err);
  } finally {
    loading.value = false;
  }
}

function getURL(endpoint) {
  let host = "https://charging-twin-qw8ag.ondigitalocean.app";

  if (
    window.location.hostname === "localhost" ||
    window.location.hostname === "127.0.0.1"
  ) {
    host = "http://localhost:8000";
  }

  return host + endpoint;
}

let chargeMask = [
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
];

function updateColorStatesAndRefreshData(series, newData) {
  series.data.setAll(newData);
}




// --------------------- WEBSOCKETS ----------------------------
// ---------------------------------
// ---------------------------------
// ---------------------------------



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

    let batteryResponseCharge = data?.car?.battery_percentage;

    if (batteryResponseCharge != undefined) {
      batteryPercentage.value = batteryResponseCharge;
    }

    let batteryResponseHours = data?.car?.estimated_time_until_full;

    carState.value = data?.car?.car_state;

    if (batteryResponseHours != undefined) {
      let timeString = batteryResponseHours;
      let hour = parseInt(timeString, 10); // The second parameter 10 specifies the base for parsing.
      batteryHours.value = hour;
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
.circle-container {
  width: 100vh;
  height: 100vh;
  position: relative;
  background: rgb(0, 0, 0);
  overflow: hidden;
}

#chartdiv {
  width: 114%;
  height: 114%;
  margin: -7%;
}

.rotating-dial {
  position: absolute;
  width: 64%;
  height: 64%;
  top: 18%;
  left: 18%;
  border-radius: 50%;
  background: conic-gradient(
    transparent 0%,
    #fff 0.1%,
    #fff 4%,
    transparent 4.1%,
    transparent
  );
  z-index: 1;
}

.rotating-dial-2 {
  position: absolute;
  width: 64%;
  height: 64%;
  top: 18%;
  left: 18%;
  border-radius: 50%;
  background: conic-gradient(
    #121212 0%,
    #e49623 0.1%,
    #e49623 2%,
    #121212 2.1%,
    #121212
  );
  rotate: 80deg;
  pointer-events: none;
  z-index: 0;
}

.circle-inside {
  position: absolute;
  width: 56%;
  height: 56%;
  top: 22%;
  left: 22%;
  z-index: 2;
  background: rgb(0, 0, 0);
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  border-radius: 50%;
  user-select: none;
  pointer-events: none;
}

.clock {
  font-size: 2em;
  margin-top: -32px;
  margin-bottom: 0px;
}

.deadline-clock {
  font-size: 8em;
  color: white;
  font-weight: 600;
}

.charge-indicator {
  color: white;
  background: #1db655;
  padding: 0px 16px;
  border-radius: 24px;
  font-size: 1.6em;
}

.charge-deadline {
  margin-top: -40px;
  margin-bottom: 24px;
  font-size: 1.4em;
}


/* we will explain what these classes do next! */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 330ms ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

</style>
