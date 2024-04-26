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
		<!-- <video id="video" width="600" height="450" autoplay></video> -->
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

const detectionOptions = {
	withLandmarks: true,
	withDescriptors: true,
	minConfidence: 0.5,
	MODEL_URLS: {
		Mobilenetv1Model:
			"https://raw.githubusercontent.com/ml5js/ml5-data-and-models/main/models/faceapi/ssd_mobilenetv1_model-weights_manifest.json",
		FaceExpressionModel:
			"https://raw.githubusercontent.com/justadudewhohacks/face-api.js/master/weights/face_expression_model-weights_manifest.json",
		TinyFaceLandmarkModel:
			// "https://raw.githubusercontent.com/justadudewhohacks/face-api.js/master/weights/face_landmark_68_model-weights_manifest.json",
			"https://raw.githubusercontent.com/justadudewhohacks/face-api.js/master/weights/tiny_face_detector_model-weights_manifest.json",
		FaceLandmark68TinyNet:
			"https://raw.githubusercontent.com/justadudewhohacks/face-api.js/master/weights/face_landmark_68_model-weights_manifest.json",
		FaceRecognitionModel:
			"https://raw.githubusercontent.com/justadudewhohacks/face-api.js/master/weights/face_recognition_model-weights_manifest.json",
	},
};

Promise.all([
	faceapi.nets.ssdMobilenetv1.loadFromUri(detectionOptions.MODEL_URLS.Mobilenetv1Model),
	faceapi.nets.tinyFaceDetector.loadFromUri(
		detectionOptions.MODEL_URLS.TinyFaceLandmarkModel
	),
	faceapi.nets.faceLandmark68Net.loadFromUri(
		detectionOptions.MODEL_URLS.FaceLandmark68TinyNet
	),
	faceapi.nets.faceRecognitionNet.loadFromUri(
		detectionOptions.MODEL_URLS.FaceRecognitionModel
	),
	faceapi.nets.faceExpressionNet.loadFromUri(
		detectionOptions.MODEL_URLS.FaceExpressionModel
	),
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
			const video = document.getElementById('video')
			video.srcObject = stream

			function getLabeledFaceDescriptions() {
				const labels = ["Felipe", "Fiona", "Visard"];
				return Promise.all(
					labels.map(async (label) => {
						const descriptions = [];
						for (let i = 1; i <= 2; i++) {
							const img = await faceapi.fetchImage(`./src/labels/${label}/${i}.png`);
							const detections = await faceapi
								.detectSingleFace(img)
								.withFaceLandmarks()
								.withFaceDescriptor();
							descriptions.push(detections.descriptor);
						}
						return new faceapi.LabeledFaceDescriptors(label, descriptions);
					})
				);
			}

			video.addEventListener("play", async () => {
				const labeledFaceDescriptors = await getLabeledFaceDescriptions();
				const faceMatcher = new faceapi.FaceMatcher(labeledFaceDescriptors);

				const canvas = faceapi.createCanvasFromMedia(video);
				document.body.append(canvas);

				const displaySize = { width: video.width, height: video.height };
				faceapi.matchDimensions(canvas, displaySize);

				setInterval(async () => {
					const detections = await faceapi
						.detectAllFaces(video)
						.withFaceLandmarks()
						.withFaceDescriptors();

					const resizedDetections = faceapi.resizeResults(detections, displaySize);

					canvas.getContext("2d").clearRect(0, 0, canvas.width, canvas.height);

					const results = resizedDetections.map((d) => {
						return faceMatcher.findBestMatch(d.descriptor);
					});
					results.forEach((result, i) => {
						const box = resizedDetections[i].detection.box;
						const drawBox = new faceapi.draw.DrawBox(box, {
							label: result,
						});
						drawBox.draw(canvas);
					});
				}, 100);
			});
		},
		function (error) {
			console.error(error)
		}
	)
})




</script>
<style scoped>

</style>
