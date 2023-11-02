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