<script>
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
          let response = await fetch("http://127.0.0.1:5000/category");
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
      <ul v-for="(category, index) in categories" :key="category.id">
        <div v-if="index <= numCategories">
          <p>{{ category.id }}</p>
          <li>{{ category.name }}</li>
          <p>{{ category.depense }}</p>
        </div>
      </ul>
    </div>
</template>
>>>>>>> 7e29300e12967d31df07b8aa8d6bff03b304d383
