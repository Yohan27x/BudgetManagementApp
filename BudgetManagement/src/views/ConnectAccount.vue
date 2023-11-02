<script>

import axios from 'axios'

export default{
    data(){
        return{
            username: " ",
            password: " ",
        }
    },
    methods: {
        async submit(){
        try{
            const response = await axios.post("http://127.0.0.1:8000/auth/token",{
                username: this.username,
                password: this.password
            });

            localStorage.setItem("token", response.data.token )
            console.log(localStorage.getItem("token"))

            this.$router.push('menu')
        } catch(error){
            console.error(error)
        }
    },
    computed: {
        username : {
            set(newValue){
                console.log(newValue);
            },
            
        },
        password: {
            set(newValue){
                console.log(newValue);
            }
        }
        

    }
    }
}






</script>


<template>

    <div class="main">
        <h1>connect to your account</h1>
        <div class="component">
            <p>Email: {{ username }}</p>
            <input v-model="username" placeholder="enter your email" />
        </div>

        <div class="component">
            <p>password: {{ password }}</p>
            <input v-model="password" placeholder="enter your password" />
        </div>
        
        
        <div class="connect">
            <button @click="submit()">Connection</button>
        </div>
        
        
    </div>
    

</template>


<style scoped>

.connect{
    margin-top: 30px;
}

button{
    
    margin-right: 50px;
}

.main{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

.component{
    display: flex;
    flex-direction: column;
    align-items: center;
}

</style>