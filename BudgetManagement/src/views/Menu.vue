<script>

import Category from '@/components/Category.vue'


export default {
    components: {
      Category,
    },
    data() {
        return {
        
        }
    },
    computed: {
        
    },
    methods: {
        
    },
}

</script>



<template>

<main class="wrapper">

  <div id="col" class="budget">
    <h1>budget</h1>
    <h1>1000$</h1>
    <button @click="$router.push('add-expense')">new expense</button>
  </div>

  <div class="categories">

    <Category numCategories="3" />
   
  </div>

  <div class="expenses">

    <h1>last expenses</h1>

  <table>
      <tr>
        <th>Category</th>
        <th>Desc</th>
        <th>Price</th>
      </tr>
      <tr>
        <td>Alfreds Futterkiste</td>
        <td>Maria Anders</td>
        <td>Germany</td>
      </tr>
      <tr>
        <td>Centro comercial Moctezuma</td>
        <td>Francisco Chang</td>
        <td>Mexico</td>
      </tr>
  </table>

  </div>

  <div class="stats">
    <div class="piechart"></div> 

  </div>
</main>

    
</template>


<style scoped>


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
  border: 2px solid rgb(233 171 88);
  border-radius: 5px;
  background-color: rgba(233 171 88 / 0.5);
  padding: 1em;
  color: #d9480f;
}

.wrapper > div {
  border: 2px solid rgb(233 171 88);
  border-radius: 5px;
  background-color: rgba(233 171 88 / 0.5);
  padding: 1em;
  color: #d9480f;
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

div{
    display: flex;
    justify-content: flex-start;
    align-items: center;
    flex-direction: column;
}

#col{
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
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


h1{
  font-size: large;
}
</style>