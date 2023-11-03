<script>

import axios from 'axios'

export default{
    data(){
        return{
            username: '',
            password: '',
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
    fetchData() {
      const url = 'http://127.0.0.1:8000/categories';
      //const accessToken = '<your_access_token>';

      axios.get(url, {
        headers: {
          'Accept': 'application/json',
          'Authorization': 'Bearer' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJpZCI6MSwiZXhwIjoxNjk5MDE4MzQ1fQ.YEVcsi_fZhjdsMpeFNjKUkvZ4wDfG5AoTX_giuTWFPA'
        }
      })
      .then(response => {
        console.log(response.data);
        // Process the response data here
      })
      .catch(error => {
        console.error('Error:', error);
        // Handle errors here
      });
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



</script>


<template>

    <div class="main">
        <h1>connect to your account</h1>
        <div class="component">
            <p>username: {{ username }}</p>
            <input v-model="username" placeholder="enter your email" />
        </div>

        <div class="component">
            <p>password: {{ password }}</p>
            <input v-model="password" placeholder="enter your password" />
        </div>
        
        
        <div class="connect">
           <button @click="fetchData">connect</button>
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