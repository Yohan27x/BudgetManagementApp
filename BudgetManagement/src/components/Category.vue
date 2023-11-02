<script>
  import axios from 'axios'
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
          let response = await axios.get("http://127.0.0.1:8000/categories");
          this.categories = await response.json();;
        } catch (error) {
          console.log(error);
        }
      },
    },
    created() {
      this.getData();
    },
  };

</script>

<template>

      <table>

          <tr>
            <th>Category</th>
            <th>Desc</th>
            <th>Price</th>
          </tr>

          <tr v-for="(category, index) in categories" :key="category.id">
              <td>{{ category.user_id }}</td>
              <td>{{ category.name }}</td>
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
