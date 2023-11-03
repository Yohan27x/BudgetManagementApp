<script>

import Category from '@/components/Category.vue'
import { ref } from 'vue';

export default {
    components: {
      Category
    },
    data(){
      return{
        numCat : 1,
        catName : [],
        ex1Selected : ref(0),
      }
    },
    methods : {
      async getCategoryName() {
        try {
          let response = await fetch("http://127.0.0.1:5000/category-name");
          this.catName = await response.json();
          this.catName = Object.keys(this.catName)
          console.log(this.catName)
         
        } catch (error) {
          console.log(error);
        }
      },
    },
    created() {
      this.getCategoryName();
    },
    
}

</script>

<template>

  <h1 class="user-category">Your Categories</h1>
  <Category numCategories="3" />

  <br>
  <br>

    <div class="d-flex flex-column">
      <div class="col-md-3">
        <BFormSelect v-model="ex1Selected" :options="catName"/>
      </div>   
      <br>
      <BButton class="col-md-1" variant="success">Add category</BButton>
    </div>
    

</template>

<style scoped>

h1{
  font-size: 130%;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

h1.user-category{
  margin-left: 880px;
  font-size: 200%;
  margin-bottom: 50px;
  margin-top: 50px;
}




</style>