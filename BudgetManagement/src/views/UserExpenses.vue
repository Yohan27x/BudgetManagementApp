<script>

import Expenses from '@/components/Expenses.vue'

export default {
    components: {
        Expenses
    },
    data(){
      return{
        numExp : 1,
      }
    }
    
}

</script>

<template>

    <h1 class="user-expense">Your expenses</h1>
    <div class="expenses">
      <Expenses numExpenses="10" />
    </div>
  
</template>

<style scoped>

h1{
  font-size: 130%;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

h1.user-expense{
  margin-left: 880px;
  font-size: 200%;
  margin-bottom: 50px;
  margin-top: 50px;
}


</style>