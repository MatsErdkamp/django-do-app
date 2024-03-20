<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <nav>
    <RouterLink to="/charge">
      <img src="@/assets/svgs/bolt.svg" />

      Charge</RouterLink
    >
    <RouterLink to="/counter">
      <img style="width: 28px" src="@/assets/svgs/counter.svg" />Counter
    </RouterLink>
  </nav>
  <main>
    <RouterView />
  </main>
</template>

<style scoped>


nav {
  width: 100%;
  font-size: 12px;
  position: fixed;
  bottom: -2px;
  left: 0;
  font-size: 0.8em;
  background: black;
  display: flex;
  border-top: 1px solid #212121;
  align-items: flex-start;
  justify-content: flex-start;
}



nav a.router-link-exact-active {
  opacity: 1;
  background: radial-gradient(at center bottom, rgb(20,20,20), transparent 50%);
}

nav a {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  flex-direction: column;
  font-size: 0.8em;
  opacity: 0.5;
  color: white;
  min-width: 60px;
  flex: 1;
  padding: 8px 0;
}


nav a img {
  width: 28px;
  margin-bottom: 4px;
}

</style>
