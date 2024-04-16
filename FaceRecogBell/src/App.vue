<template>
	<header>

		<div v-if="userStore.username">
			<navbar2 />
		</div>
		<div v-else>
			<navbar1 />
		</div>
	</header>

	<body>
		<video id="video" width="600" height="450" autoplay></video>
	</body>

	<RouterView />
</template>
<script>
import { RouterLink, RouterView } from 'vue-router'
import { defineComponent, onMounted } from "vue";
import navbar1 from '@/components/navbar1.vue';
import navbar2 from '@/components/navbar2.vue';
import { useUserStore } from '../src/stores/auth'
import * as faceapi from 'face-api.js';

export default defineComponent({
	components: {
		RouterView,
		navbar1,
		navbar2
	},
	setup() {
		const userStore = useUserStore();



		return { userStore };
	}
});

Promise.all([
	faceapi.nets.ssdMobilenetv1.loadFromUri("/models"),
	faceapi.nets.faceRecognitionNet.loadFromUri("/models"),
	faceapi.nets.faceLandmark68Net.loadFromUri("/models"),
]).then(() => {
	navigator.getUserMedia = navigator.getUserMedia ||
            navigator.webkitGetUserMedia ||
            navigator.mozGetUserMedia;

        // Start video camera
        navigator.getUserMedia({
                video: true,
                audio: false
            },
            function (stream) {
              document.getElementById('video').srcObject = stream
            },
            function (error) {
              console.error(error)
            }
        )
})



</script>
<style scoped></style>
