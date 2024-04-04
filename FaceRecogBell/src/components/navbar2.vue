<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/">Home</router-link>
          <ul class="navbar-nav .navbar-right">
            <li><router-link class="nav-link" @click="submitLogin">Log ut</router-link></li>
          </ul>
        </div>
      
    </nav>
</template>
  
<script>
	import { defineComponent } from "vue";
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
  