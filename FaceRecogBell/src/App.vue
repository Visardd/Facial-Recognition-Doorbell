<template>
	<header>

		<div v-if="userStore.username">
			<navbar2 />
			<div>
				<h1>Welcome, {{ userStore.username }}!</h1>
				<p>Thank you for logging in.</p>
			</div>
		</div>
		<div v-else>
			<navbar1 />
			
				<div>
					<h1>Welcome to FaceRecogBell!</h1>
					<p>Please sign in or create an account to continue.</p>
				</div>
			
		</div>
	</header>

	

	<RouterView />
</template>
<script>
import { RouterLink, RouterView } from 'vue-router'
import { defineComponent, onMounted } from "vue";
import navbar1 from '@/components/navbar1.vue';
import navbar2 from '@/components/navbar2.vue';
import { useUserStore } from '../src/stores/auth'



export default defineComponent({
	components: {
		RouterView,
		navbar1,
		navbar2,
	},
	setup() {
		const userStore = useUserStore();

		return { userStore };
	}
});



</script>
<style scoped>

</style>
