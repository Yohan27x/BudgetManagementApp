<script>
  export default {
    props: {
      numExpenses: Number,
    },
    data() {
      return {
        expenses: [],
      };
    },
    methods: {
      async getData() {
        try {
          let response = await fetch("http://127.0.0.1:5000/category");
          this.expenses = await response.json();;
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
      <ul v-for="(expense, index) in expenses" :key="expense.id">
        <div v-if="index <= numExpenses">
          <p>{{ expense.id }}</p>
          <li>{{ expense.name }}</li>
          <p>{{ expense.depense }}</p>
        </div>
      </ul>
    </div>
</template>