<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">Home</router-link>
        <ul class="navbar-nav .navbar-right">
          <li><router-link class="nav-link" to="/Login">Login</router-link></li>
          <li><router-link class="nav-link" to="/Signup">Sign Up</router-link></li>
        </ul>
      </div>
    
  </nav>
</template>

<script>
  import { defineComponent } from "vue";
  
</script>
