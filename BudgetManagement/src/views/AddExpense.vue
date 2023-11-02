<script>
import { ref } from 'vue';


export default {
  methods: {
      async getData() {
        try {
          let response = await fetch("http://127.0.0.1:5000/category-name");
          this.ex1Options = await response.json();;
        } catch (error) {
          console.log(error);
        }
      },
    },

    data() {
      return {
       
        ex1Options : [],
        ex1Selected : ref(0),
        }
    },
    created() {
      this.getData();
    }
  };

</script>


<template>

    <h1>add expense</h1>
    <h1>choose category</h1>
    <button>add expense</button>

    <div class="d-flex justify-content-center">
      <BAlert class="col-md-3 " :model-value="true" variant="primary">Primary Alert</BAlert>
    </div>
  
    <div class="d-flex flex-column">
      <div class="col-md-3">
        <BFormSelect v-model="ex1Selected" :options="ex1Options"/>
        <h1>{{ ex1Selected }}</h1>
      </div>   
    </div>



</template>


<style scoped>

</style>