<template>
  <div class="circle-container">
    <div id="chartdiv"></div>

    <div class="rotating-dial"></div>

    <div class="circle-inside">
      <div class="clock">{{ new Date().toLocaleTimeString() }}</div>

      <div class="deadline-clock">{{ chargeDeadline }}</div>
      <div class="charge-deadline">charge deadline for 'work'</div>

      <div class="charge-indicator">charging 54%</div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";

// Reactive value for chargeDeadline

const currentTime = ref("11:");
const chargeDeadline = ref("14:00");
const rotation = ref(0); // Initial rotation in degrees

onMounted(() => {
  createChart();
  handleRotation();
});

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
    var series = chart.series.push(
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

    setSeriesColor(series);

    // Set data
    var data = [];

    for (var i = 0; i < 24; i++) {
      data.push({ category: i, value: 20 });
    }

    // Add series
    // https://www.amcharts.com/docs/v5/charts/xy-chart/series/
    var series2 = chart.series.push(
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

    // Set data
    var data2 = [];

    for (var i = 0; i < 24; i++) {
      data2.push({ category: i, value: Math.round(Math.random() * 100) });
    }

    xAxis.data.setAll(data);
    series.data.setAll(data);
    series2.data.setAll(data2);

    // Make stuff animate on load
    // https://www.amcharts.com/docs/v5/concepts/animations/
    series.appear(1000);
    series2.appear(1000);
    chart.appear(1000, 100);
  });
}

const booleanMask = [
  true,
  false,
  false,
  false,
  true,
  true,
  true,
  false,
  true,
  false,
  false,
  false,
  true,
  true,
  true,
  false,
  true,
  false,
  false,
  false,
  true,
  true,
  true,
  false,
];

function setSeriesColor(series) {
  // Make each column to be of a different color
  series.columns.template.adapters.add("fill", function (fill, target) {
    if (booleanMask[series.columns.indexOf(target)] === true) {
      return "#22e66a";
    } else {
      return "#212121";
    }
  });

  series.columns.template.adapters.add("stroke", function (stroke, target) {
    if (booleanMask[series.columns.indexOf(target)] === true) {
      return "#22e66a";
    } else {
      return "#212121";
    }
  });
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
    const hours = Math.floor((val % 350) / 14.5);
    chargeDeadline.value = `${hours}:00`;

    startAngle = currentAngle;
  };

  const stopRotation = () => {
    isDragging = false;
    document.removeEventListener("mousemove", rotateDial);
    document.removeEventListener("mouseup", stopRotation);
    document.removeEventListener("touchmove", rotateDial);
    document.removeEventListener("touchend", stopRotation);
};
}
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
  background: conic-gradient(#fff 0%, #fff 4%, #121212 4%, #121212);


}

.circle-inside {
  position: absolute;
  width: 56%;
  height: 56%;
  top: 22%;
  left: 22%;

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
</style>
