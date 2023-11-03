<script>
  import axios from 'axios'
  import { ref } from 'vue';
  
  export default {
    props: {
      numCategories: Number,
    },
    data() {
      return {
        categories: [],
      };
    },
    methods: {
  
    async getCategories() {
        try {
          let response = await fetch("http://127.0.0.1:5000/category");
          this.categories = await response.json();;
        } catch (error) {
          console.log(error);
        }
      },
    },
    created() {
      this.getCategories();
    },
  };

</script>

<template>

      <table>

          <tr>
            <th>Index</th>
            <th>Name</th>
            <th>Total spent</th>
          </tr>

          <tr v-for="(category, index) in categories" :key="category.id">
              <td><b>{{ index }}</b></td>
              <td><b>{{ category.name }}</b></td>
              <td><b>{{ category.depense }}$</b></td>
          </tr>

      </table>


</template>

<style scoped>


table{
  width:100%
}

td{
  border: 1px solid black;
  padding: 30px; 
}

</style>
