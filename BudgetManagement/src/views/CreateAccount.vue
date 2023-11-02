<script>

export default{
    data(){
        return{
            username: String,
            password: String,
        }
    },
    async submit(){
        try{
            const response = await axios.post("http://127.0.0.1:8000/auth",{
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

        <div class="create">
            <button @click="submit">Create Account f</button>
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