<template>
  <Head />
  <Nav />
  <Home />
</template>

<script>
import Home from "./components/Home.vue";
import Nav from "./components/Nav.vue";
import Head from "./components/Head.vue";

export default {
  name: "App",
  components: {
    Home,
    Nav,
    Head
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
