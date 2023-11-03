<script>
  import axios from 'axios'
  
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
     
    async getExpenses() {
        try {
          let response = await fetch("http://127.0.0.1:5000/category-name");
          this.expenses = await response.json();
          console.log(this.expenses)
        } catch (error) {
          console.log(error);
        } 
      },
    },
    created() {
      this.getExpenses();
    },
  };

</script>

<template>

      <table>
          <tr>
            <th>Category</th>
            <th>Desc</th>
            <th>Cost</th>
          </tr>

          <tr v-for="(expense, index) in expenses" :key="expense.id">
              <td>{{ expense.category }}</td>
              <td>{{ expense.desc }}</td>
              <td>{{ expense.price }}</td>
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
