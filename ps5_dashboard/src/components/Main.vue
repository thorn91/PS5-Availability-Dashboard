<template>
  <div>
    <h1 id="title" class="text-lg-center">PS5 Availability Dashboard</h1>
    <div id="main-container" class="d-flex justify-content-center">
      <div class="card" style="width: 24rem;">
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
<style scoped>
#title {
  margin-top: 5%;
}

#main-container {
  height: 100%;
  margin-top: 20%;
}

</style>
