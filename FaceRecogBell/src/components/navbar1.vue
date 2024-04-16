<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">Home</router-link>
        <ul class="navbar-nav .navbar-right">
          <li><router-link class="nav-link" to="/Login">Login</router-link></li>
          <li><router-link class="nav-link" to="/Signup">Sign Up</router-link></li>
          <!-- <li class="nav-link" @click="submitLogout">Log out</li> -->
        </ul>
      </div>
    
  </nav>
</template>

<script>
	import { defineComponent } from "vue";
  import { client } from "../axios"
	export default defineComponent({
		methods: {
			submitLogout() {
				return client.post(
					"/logout/", {}
				).then(function () {
					console.log("Logged out")
					return true
				}).catch(function () {
					console.log("Didn't log out")
					return false
				})
			}
		}
	})
</script>
