<script>
import axios from 'axios';

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
      async getData() {
        try {
          await axios.get("http://127.0.0.1:5000/category").then(response => (this.categories = response.data));
          this.categories = JSON.parse(this.categories)
          console.log(this.categories)
        } catch (error) {
          console.log(error);
        }
      },
    },
    mounted() {
      this.getData();
    },
  };

</script>

<template>
<<<<<<< HEAD


      <table>

          <tr>
            <th>Category</th>
            <th>Desc</th>
            <th>Price</th>
          </tr>

          <tr v-for="(category, index) in categories" :key="category.id">
              <td>{{ category.id }}</td>
              <td>{{ category.name }}</td>
              <td>{{ category.depense }}</td>
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
=======
    <div>
      <div v-for="(category,index) in this.categories" :key="category.id">
        <div v-if="index <= numCategories">

          <div>
            <p>{{ category.id }}</p>
            <p>{{ category.name }}</p>
            <p>{{ category.depense }}</p>
          </div>
          
        </div>
      </div>
    </div>
</template>
>>>>>>> 7e29300e12967d31df07b8aa8d6bff03b304d383
