<template>
  <nav class="navbar navbar-expand-md navbar-dark  bg-dark">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <router-link class="nav-link" to="/">Home</router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link" to="/statistics">Statistics</router-link>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/vulnerabilites">Vulnerebilities</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/profile">Profile</a>
      </li>
    </ul>
    <div class="mt-2 mt-md-0">
      <h2 class="mb-0 text-white">ROUTER</h2>
    </div>
  </nav>
  <router-view />
</template>
