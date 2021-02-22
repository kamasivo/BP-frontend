<template>
  <main role="main">
    <div
      class="alert alert-success d-flex justify-content-center mt-3"
      role="alert"
    >
      <h4 class="alert-heading mb-0">All safe!</h4>
    </div>
    <div class="warningWrapper mt-3" v-bind:class="{ open: showMore }"
 v-on:click="showMore = !showMore"
>
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
  </main>
</template>

<script>
export default {
  name: "Home",
  data () {
    return {
      showMore: false
    }
  },
};
</script>

<style scoped>
.dropdown-content {
  display: none;
  background-color: #f2aaa5;
  border-bottom-right-radius: 11px;
  border-bottom-left-radius: 11px;
}
.warningWrapper {
  border-radius: 11px;
  background-color: #f72e1f;
  cursor: pointer;
}
.warningWrapper.open .dropdown-content {
  display: flex;
}
.warningWrapper.open .arrow {
  transform: rotate(180deg);
  transition: 0.6s;
}
.arrow {
  font-size: 30px;
}
</style>
