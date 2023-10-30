
  
<script>
  export default {
    data() {
      return {
        posts: [],
      };
    },
  
    methods: {
      async getData() {
        try {
          let response = await fetch("http://jsonplaceholder.typicode.com/posts");
          this.posts = await response.json();;
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
      <ul v-for="post in posts" :key="post.id">
        <p>{{ post.id }}</p>
        <li>{{ post.title }}</li>
        <p>{{ post.body }}</p>
      </ul>
    </div>
  </template>