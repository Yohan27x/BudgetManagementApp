<script>

import Category from '@/components/Category.vue'
import Expenses from '@/components/Expenses.vue'

import axios from 'axios'

export default {
    components: {
      Category,
    },
    data() {
        return {
          user : null,
          budget : Number,
        }
    },
    computed: {
        
    },
    methods: {
      async UpdateBudget() {
        axios.post('http://127.0.0.1:5000/budget/', {
          total: 1000,
        })
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
      },
      async getData() {
        axios.get('http://127.0.0.1:5000/budget/1')
        .then(response => {
            this.budget = response.data;
          })
          .catch(error => {
              console.log("error")
          });
      },
    },
    created(){
      this.getData();
    }
    
}

</script>

<template>

<h1 class="welcome">Welcome to your Dashboard ! </h1>
<main class="wrapper">

  <div id="col" class="budget">
    <h1>Budget : <b>{{ this.budget["total"] }}$</b></h1>
    <BButton  @click="$router.push('add-expense')" variant="light">Add expense</BButton>
  </div>

  <div class="categories">
    <Category numCategories="3" />
  </div>

  <div class="expenses">
    <Expenses numExpenses="3" />
  </div>


  <div class="stats">
    <div class="piechart"></div> 
  </div>
</main>

    
</template>


<style scoped>

.welcome{
  margin-left: 725px;
  font-size: 210%;
  margin-bottom: 50px;
  margin-top: 50px;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}


* {
  box-sizing: border-box;
}
.wrapper {
  max-width: 3000px;
  max-height: 2000px;
  margin: 0 auto;
  margin-top: 40px;
}

.wrapper > div {
  border: 2px solid rgb(25, 30,74);
  border-radius: 5px;
  background-color: rgba(141, 172, 202);
  padding: 1em;
}


.wrapper {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  gap: 10px;
  grid-auto-rows: minmax(150px, auto);
}
.budget {
  grid-column: 1/3;
  grid-row: 1;
}
.expenses {
  grid-column: 1 / 3;
  grid-row: 2 / 4;
}
.categories {
  grid-column: 3/4;
  grid-row: 1/3;
}
.stats {
  grid-column: 3/5;
  grid-row: 3/4;
}

.stats:hover{
  border: 2px solid white;
}

.categories:hover{
  border: 2px solid white;
}

.expenses:hover{
  border: 2px solid white;
}

.budget:hover{
  border: 2px solid white;
}

div{
    display: flex;
    justify-content: flex-start;
    align-items: center;
    flex-direction: column;
}

#col{
    display: flex;
    flex-direction: row;
    justify-content: center;
  
    
    gap: 50px;

}

table{
  width:100%
}

td{
  border: 1px solid black;
  padding: 30px; 
}


.piechart { 
            display: block; 
            width: 100px; 
            height: 100px; 
            border-radius: 50%; 
            background-image: conic-gradient( 
                pink 70deg,  
                lightblue 0 235deg,  
                orange 0); 
        } 
  
        body, 
        .piechart { 
            display: flex; 
            justify-content: center; 
            align-items: center; 
        } 



</style>