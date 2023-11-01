<script>

import Category from '@/components/Category.vue'

export default {
    components: {
      Category
    },
    data(){
      return{
        numCat : 1,
      }
    }
    
}

</script>

<template>

  <h1>categories user</h1>
  <Category numCategories="3" />

  <h1>add category</h1>
  <button>add</button>
  

</template>

<style>

</style>