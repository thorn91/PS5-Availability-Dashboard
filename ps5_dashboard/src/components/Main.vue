<template>
 <div id="main-container" class="d-flex justify-content-center">
    <div class="card" style="width: 24rem;">
      <ul class="list-group p-1 list-group-flush">
        <!-- Individual template items have to be individual, too many differences -->
        <Walmart />
        <li class="list-group-item">A second item</li>
        <li class="list-group-item">A third item</li>
      </ul>
    </div>
  </div>
</template>

<script>
import Walmart from './Walmart.vue'

export default {
  components: { Walmart },
  name: 'Main',
  props: {
    Walmart,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#main-container {
  height: 100%;
  margin-top: 25%;
}

</style>
