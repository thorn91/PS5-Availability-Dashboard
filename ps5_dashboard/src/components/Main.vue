<template>
  <div id="main-container" class="">
    <p id="title" class="text-center fs-1 font-monospace light">PS5 Availability Dashboard</p>
    <div id="card-container" class="d-flex justify-content-center row">
      <div class="card row bg-transparent" style="width: 24rem;">
        <ul class="list-group p-1 list-group-flush">
          <!-- Individual template items have to be separate, too many differences -->
          <Walmart />
          <Target />
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import Walmart from './Walmart.vue'
import Target from './Target.vue'

export default {
  components: { Walmart, Target },
  name: 'Main',
  props: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
body {
  background-color: #DFDBE5;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4' viewBox='0 0 4 4'%3E%3Cpath fill='%23b0a9bc' fill-opacity='0.4' d='M1 3h1v1H1V3zm2-2h1v1H3V1z'%3E%3C/path%3E%3C/svg%3E");
}

#main-container {
  height: 100%;
}

#title {
  margin-top: 5%;
}

#card-container {
  /* height: 100%; */
  margin-top: 20%;
}

p {
  font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

.list-group-item {
  opacity: .85;
}

</style>
