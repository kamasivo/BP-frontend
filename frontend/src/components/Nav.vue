<template>
  <nav class="navbar navbar-expand-md navbar-dark  bg-dark">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <router-link :active="isActive" class="nav-link" to="/"
          >Home</router-link
        >
      </li>
      <li class="nav-item">
        <router-link :active="isActive" class="nav-link" to="/statistics"
          >Network statistics</router-link
        >
      </li>
      <li class="nav-item">
        <router-link :active="isActive" class="nav-link" to="/devices">
          Vulnerabilities
        </router-link>
      </li>
    </ul>
    <div class="mt-2 mt-md-0">
      <h2 class="mb-0 text-white">NETWORK SCANNER</h2>
    </div>
  </nav>
  <router-view />
</template>

<style scoped>
.router-link-active {
  color: white !important;
}
</style>
