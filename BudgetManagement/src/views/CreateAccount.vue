<script>

export default{
    data(){
        return{
            email: String,
            password: String,
            confirmPassword: String
        }
    },
    computed: {
        email : {
            set(newValue){
                console.log(newValue);
            },
            
        },
        password: {
            set(newValue){
                console.log(newValue);
            }
        },
        confirmPassword: {
            set(newValue){
                console.log(newValue);
            }
        }

    }

}





</script>


<template>

    <div class="main">
        <h1>create your account</h1>
        <div class="component">
            <p>Email: {{ email }}</p>
            <input v-model="email" placeholder="enter your email" />
        </div>

        <div class="component">
            <p>password: {{ password }}</p>
            <input v-model="password" placeholder="enter your password" />
        </div>

        <div class="component">
            <p>confirm Password: {{ confirmPassword }}</p>
            <input v-model="confirmPassword" placeholder="enter your password" />
        </div>

        <div class="create">
            <button>Create Account</button>
            <router-link to="/connect">already have an account ? </router-link>
        </div>
        

        
        
        
        
    </div>
    

</template>


<style scoped>

.create{
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