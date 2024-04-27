<template>
	<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
	  <div class="container-fluid">
		<router-link class="navbar-brand" to="/">Home</router-link>
		  <ul class="navbar-nav .navbar-right">
			<li><router-link class="nav-link" to="/profile">View Profile</router-link></li>
			<li><router-link class="nav-link" to="/cameraview">View Camera</router-link></li>

			<li class="nav-link" @click="submitLogout">Logout</li>
			

		  </ul>
		</div>
	  
	</nav>
</template>


<script>

	import { client } from "../axios"

	import { defineComponent } from "vue";
	import { useUserStore } from "@/stores/auth";

	export default defineComponent({
		methods: {
			submitLogout() {
				return client.post(
					"/logout/", {
						// withCredentials: true,
					}
				).then(function () {
					const userStore = useUserStore();
					userStore.logout()
					return true
				}).catch(function () {
					console.log("Didn't log out")
					return false
				})
			}
		}
	})
</script>
  