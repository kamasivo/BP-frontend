<template>
  <div
    class="alert alert-success d-flex justify-content-center mt-3"
    role="alert"
  >
    <h4 class="alert-heading mb-0">All safe!</h4>
  </div>
  <div class="warningWrapper mt-3">
    <div class="d-flex align-items-center pt-2 pb-2">
      <h2 class="ml-3 mt-2 text-white">
        WARNING - [DEVICE NAME] has vulnerability
      </h2>
      <i class="fas fa-arrow-down arrow ml-auto mr-5 text-white"></i>
    </div>

    <div class="dropdown-content">
      <p class="ml-3 mt-2">CONTENT TEXT WILL GO HERE</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  props: {
    msg: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
