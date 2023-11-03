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
        price: ref(0),
        }
    },
    created() {
      this.getData();
    }
  };

</script>


<template>


  <div>

    <div class="d-flex flex-column">
        <div class="col-md-3">
          <h1>Choose category</h1>
          <BFormSelect v-model="ex1Selected" :options="ex1Options"/>

        </div>   
      </div>
  </div>
  

  <div class="d-flex flex-column">
    <div class="col-md-3"> 
      <h1>Depense price</h1>
      <BFormInput v-model="price" placeholder="Enter the depense price" />
      <BButton variant="success">Add expense</BButton>
    </div>
  </div>
    

   
    

</template>


<style scoped>

button{
  margin-top : 30px;
}

.col-md-3{
  margin-top: 20px;
  margin-left: 60px;
}

h1{
  margin-top: 10px;
  margin-left: 50px;
  font-size: 130%;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

</style>