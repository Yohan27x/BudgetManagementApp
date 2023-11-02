<script>

import NavBar from "@/components/Navbar.vue"

export default {
    components: {
        NavBar
    },
    data() {
        return {
            email : "",
            password: "",
            username: "",
        }
    },
    computed: {
        email: {
            set(value){
                console.log(value);
            }
        }
    },
    methods: {
        
    },
}

</script>


<template>

    <!-- get the user name -->
    <h1>{{message}} PROFIL</h1>

    <div class="info">
        <div class="field">
            <p id="marge">EMAIL ADRESS :</p>
             <!-- <p id="marge">EMAIL ADRESS : {{ message }}</p> -->
            <input v-model="email" placeholder="edit me" />
            <button>modify</button>
        </div>

        <div class="field">
            <p>USERNAME</p>
            <input v-model="username" placeholder="edit me" />
            <button>modify</button>
        </div>

        <div class="field">
            <p>PASSWORD :</p>
            <input v-model="password" placeholder="edit me" />
            <button>modify</button>
        </div>
<<<<<<< HEAD
<<<<<<< HEAD

        <BButton variant="success">Button</BButton>
        
=======
>>>>>>> 7e29300e12967d31df07b8aa8d6bff03b304d383


        <button>disconnect</button>
=======
>>>>>>> 6bef57048434890468e0d735f4844c6d6cc85a6b
        

        <br>
    </div>
    
</template>


<style scoped>



h1{
    display: flex;
    align-items: center;
    justify-content: center;
}

.info{
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

.field{
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: row;
    justify-content: space-evenly;
    gap: 50px;
    
}

#marge{
    margin-right: -27px
}


</style>