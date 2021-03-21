<template>
  <Head />
  <Nav />
</template>

<script>
import Nav from "./components/Nav.vue";
import Head from "./components/Head.vue";
export default {
  name: "App",
  components: {
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
  color: #2c3e50;
}
main {
  padding-left: 5%;
  padding-right: 5%;
}
.card {
  border-radius: 11px;
}
</style>
