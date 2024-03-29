<template>
  <div class="charge-content">
    <div class="background-lines">
      <div class="line-1"></div>
      <div class="line-2"></div>
      <div class="line-3"></div>
      <div class="line-4"></div>
    </div>
    <div class="background-lines-bottom">
      <div class="bottom-line-1"></div>
      <div class="bottom-line-2"></div>
      <div class="bottom-line-3"></div>
      <div class="bottom-line-4"></div>
    </div>

    <div class="charge-background-gradient"></div>

    <div class="charge-info-container">
      <div class="info-item">55%</div>

      <div>
        <div class="charging-info-indicator">
          <h1>CHARGING</h1>
        </div>
        <div class="charging-info-indicator-overlay">
          <h1>CHARGING</h1>
        </div>
      </div>

      <div class="info-item">7AM</div>
    </div>
    <div class="charge-car-container">
      <img src="@/assets/polestar.webp" alt="" />
    </div>
    <div class="charge-graph-container">
      <ChargeGraph></ChargeGraph>

      <RouterLink to="#"
        >Adjust Planning <img style="width: 24px;"
        src="@/assets/svgs/triangle.svg"
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import ChargeGraph from "@/components/ChargeGraph.vue";


</script>

<style scoped>
.charge-content {
  width: 100vw;
  height: 100%;
}

.charge-info-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: row;
  width: 100%;
  padding: 48px 9vw;
  height: 18vh;
  margin-top: 2vh;
}

.info-item {
  font-size: 1.4em;
}

.charging-info-indicator {
  border-radius: 48px;
  background: rgb(23, 160, 53);
  padding: 0px 12px;
  font-size: 0.8em;
  color: black;
  font-weight: 700;
  position: absolute;
  top: 9vh;
  transform: translateX(-50%);
  z-index: 0;
}
.charging-info-indicator-overlay {
  border-radius: 48px;
  background: transparent;
  padding: 0px 12px;
  font-size: 0.8em;
  color: transparent;
  outline: 8px solid rgb(0, 0, 0);
  font-weight: 700;
  position: absolute;
  top: 9vh;
  transform: translateX(-50%);
  z-index: -10;
}

.charging-info-indicator::before {
  content: "";
  position: absolute;
  background: linear-gradient(0deg, black, transparent);
  height: 5vh;
  z-index: 1;
  width: 46px;
  bottom: -13vh;
  left: 50%;
  transform: translateX(-50%);
}

.charging-info-indicator-overlay::before {
  content: "";
  position: absolute;
  background: black;
  height: 30vh;
  z-index: -1;
  width: 46px;
  top: -12vh;
  left: 50%;
  transform: translateX(-50%);
}

.charging-info-indicator::after {
  content: "";
  position: absolute;
  background: rgb(23, 160, 53);
  height: 30vh;
  z-index: -1;
  width: 12px;
  top: -12vh;
  left: 50%;
  transform: translateX(-50%);
}

.charge-car-container {
  z-index: 1000;
  position: absolute;
  background: linear-gradient(
    0deg,
    transparent,
    #050505 10%,
    transparent 60%
  );
}

.charge-car-container img {
  max-width: 100%;
  z-index: 100;
  margin-bottom: -20px;
}

.charge-background-gradient {
  position: absolute;
  top: 0;
  z-index: -1;
  width: 100%;
  height: 49vh;
  background: linear-gradient(0deg, rgba(109, 236, 147, 0.4),  rgba(36, 187, 86, 0) 100%);
}

.charge-graph-container {
  position: absolute;

  bottom: 0;
  width: 100%;
  height: 30svh;

  margin-bottom: 8svh;
}

.charge-graph-container a {
  background: white;
  padding: 4px 6px 4px 12px;
  border-radius: 8px;
  color: black;
  font-weight: 600;
  float: right;
  margin-right: 12px;
  margin-top: 8px;
  font-size: 0.9em;
  height: 30px;
  display: flex;
  align-items: center;
}

.charge-graph-container::before {
  content: "";
  position: absolute;
  background: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.8),
    rgba(0, 0, 0, 0.2) 80%
  );
  height: 50vh;
  z-index: -1;
  width: 58px;
  bottom: -5vh;
  left: 50%;
  transform: translateX(-50%);
}

.background-lines {
  width: 100vw;
  height: 50vh;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -2;
}

.background-lines-bottom {
  width: 100vw;
  height: 50vh;
  position: absolute;
  bottom: 0vh;
  left: 0;
  z-index: -2;
}

.line-1,
.line-2,
.line-3,
.line-4 {
  border-left: 1px dashed #181818;
  position: absolute;
  left: 13vw;
  height: 50vh;
}

.line-2 {
  left: unset;
  right: 13vw;
}

.line-3 {
  left: 29vw;
}

.line-4 {
  left: unset;
  right: 29vw;
}

.bottom-line-1,
.bottom-line-2,
.bottom-line-3,
.bottom-line-4 {
  border-left: 1px dashed #161616;
  position: absolute;
  left: 7vw;
  height: 50vh;
}

.bottom-line-2 {
  left: unset;
  right: 7vw;
}

.bottom-line-3 {
  left: 24vw;
}

.bottom-line-4 {
  left: unset;
  right: 24vw;
}
</style>
