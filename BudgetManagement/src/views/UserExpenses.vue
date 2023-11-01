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

    <h1>Expenses user</h1>
    <Expenses numExpenses="3" />
  

</template>

<style>

</style>