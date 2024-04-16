<template>
	<div class="container mt-5">
		<form @submit.prevent="submitLogin()" class="border p-4 bg-light">
			<h2 class="mb-4 text-center">Log In!</h2>

			<div v-if="loginError" class="alert alert-danger">
				{{ loginErrorMessage }}
			</div>

			

			<!-- Username Field -->
			<div class="form-group mb-3">
				<label for="usernameInput" class="form-label">Username</label>
				<input type="text" v-model="username" class="form-control" id="usernameInput"
					placeholder="Enter username" required>
			</div>

			<!-- Password Field -->
			<div class="form-group mb-4">
				<label for="passwordInput" class="form-label">Password</label>
				<input type="password" v-model="password" class="form-control" id="passwordInput" placeholder="Password"
					required>
			</div>

			<!-- Submit Button -->
			<button type="submit" class="btn btn-primary w-100">Submit</button>
		</form>
	</div>
</template>

<script>
import { defineComponent } from "vue";
import { useUserStore } from "@/stores/auth";
import { SendLoginRequest } from "@/server/authentication";

export default defineComponent({
	
	data() {
		return {
			username: '',
			password: '',
			token: '',
			loginError: false,
			loginErrorMessage: '',

		}
	},
	methods: {
		async submitLogin() {
			let [loggedIn, username] = await SendLoginRequest(this.username, this.password)

			if (!loggedIn) {
				this.loginError = true
				this.loginErrorMessage = "eRROr"
				return
			}

			const userStore = useUserStore();
			userStore.login(username)
			this.$router.push({ path: '/' })
			
			
		}
	}
})
</script>

<style scoped></style>
