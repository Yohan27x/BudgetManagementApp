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