<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/counter">Counter</RouterLink>
  </nav>
  <main>
    <RouterView />
  </main>
</template>

<style scoped>
.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;

  position: fixed;
  top: 0;
  left: 0;
  padding: 24px 24px;
  font-size: 1.2em;
}

nav a.router-link-exact-active {
  color: rgb(12, 104, 190);
  font-weight: 400;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
}

@media (min-width: 1024px) {
  .logo {
    margin: 0 2rem 0 0;
  }
}
</style>
