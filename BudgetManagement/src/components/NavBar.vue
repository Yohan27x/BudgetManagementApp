<script>
import { callWithAsyncErrorHandling } from 'vue';


export default {
    components: {

    },
    data() {
        return {
            isActive: false,
        }
    },
    computed: {
        
    },

    mounted() {

    }
}
</script>


<template>

    <div class="navbar">
        
        <div id="menu" class="menu-selection">
            <img @click="isActive = !isActive" src="@/assets/MenuChoose.png" height="120" /> 
            <div class="under-menu">
                <router-link @click="isActive = !isActive" to="/categories" :class="{ active: !isActive }">categories</router-link>
                <router-link @click="isActive = !isActive" to="/expenses" :class="{ active: !isActive }">expenses</router-link>
                <router-link @click="isActive = !isActive" to="/stats" :class="{ active: !isActive }">stats</router-link>
            </div>
            
            
        </div>
            
            <h1>
                <router-link style="text-decoration: none; color: inherit;" to="menu">BudgetCool</router-link>
            </h1>

        <router-link class="profil" tag="div" to="/profil">
            <img src="@/assets/UserIcon.png" height="120">
        </router-link>


        

    </div>

</template>


<style scoped>


.under-menu{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    border-top: 0cap;
    border-left: 0cap;
    border-bottom: 0cap;
    border-right: 0cap;
}

.active{
    display: none
}

h1{
    font-family: 'Times New Roman', Times, serif;
    font-size: 40px;
}

div{
    border: solid;
    border-color: black;
    border-width: 0.3cap;
}

.navbar{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    
}

.menu-selection{
    width: 150px;
    margin-left: 0.5%;
    border-top: 0cap;
    border-left: 0cap;
    border-bottom: 0cap;
}

.profil{
    border: solid;
    border-color: black;
    border-width: 0.3cap;
    border-top: 0cap;
    border-right: 0cap;
    border-bottom: 0cap;
}




</style>