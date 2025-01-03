<template>

    <body>
        <div>
            <video id="video" width="600" height="450" autoplay></video>
        </div>
        <div class="d-flex justify-content-center">
            <div class=" justify-content-center">
                <input type="file" class="form-control" @change="onFileChange">
                <input type="text" class="form-control" v-model="category" placeholder="Enter category">
                <button class="btn btn-primary" @click="uploadImage">Upload Image</button>
                <button class="btn btn-secondary" @click="addName">Add name</button>
            </div>

            <div v-if="uploadSuccess" class="alert alert-success mt-3">File uploaded successfully!</div>
            <div v-else class="alert alert-danger mt-3">Please select an image and enter a category</div>

            <div v-if="imagePreview">
                <h3>Image Preview:</h3>
                <img :src="imagePreview" alt="Preview" width="200">
            </div>
        </div><br>
        <div class="d-flex justify-content-center">
            <button class="btn btn-primary" @click="clearNotifications">Clear Notifications</button>
            <div class="Log" id="detection-log"
                style="position: fixed; right: 0; top: 60px; width: 300px; background: rgba(255,255,255,0.9); padding: 10px; height: 90vh; overflow-y: auto;">

                <!-- here is where notifications are spawned in -->
            </div>
        </div>
    </body>
</template>

<script>
import { defineComponent, onMounted } from "vue";
import { useUserStore } from '../stores/auth'
import * as faceapi from 'face-api.js';
import axios from 'axios';

export default defineComponent({
    data() {
        return {
            image: null,
            category: '',
            uploadSuccess: false,
            imagePreview: null,
            labels: [],
        }
    },
    components: {

    }, methods: {
        addName() {
            this.labels.push(this.category);
            console.log(this.labels);
        },
        onFileChange(e) {
            this.image = e.target.files[0];
            this.imagePreview = URL.createObjectURL(this.image); // Create a preview URL for the selected image
        },
        uploadImage() {
            if (!this.image || !this.category) {
                console.error("Please select an image and enter a category");
                // this.uploadSuccess = False;
                return;
            }

            const formData = new FormData();
            formData.append('image', this.image);
            formData.append('title', 'Sample Image');
            formData.append('category', this.category);

            axios.post('http://localhost:8000/upload/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(response => {
                    console.log(response);
                    this.uploadSuccess = true; // Set uploadSuccess to true after successful upload
                })
                .catch(error => console.error(error));
        },
        clearNotifications() {
            const detectionLog = document.getElementById('detection-log');
            detectionLog.innerHTML = '';
        }
    },
    setup() {
        onMounted(() => {
            navigator.mediaDevices.getUserMedia({ video: true })
                .then((stream) => {
                    const video = document.getElementById('video');
                    video.srcObject = stream;
                })
                .catch((error) => {
                    console.error(error);
                });
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

            navigator.getUserMedia({
                video: true,
                audio: false
            },
                function (stream) {
                    const video = document.getElementById('video')
                    video.srcObject = stream

                    function getLabeledFaceDescriptions() {
                        const labels = ["Messi", "Fiona", "Visard", "Ronaldo"];
                        return Promise.all(
                            labels.map(async (label) => {
                                const descriptions = [];
                                for (let i = 1; i <= 2; i++) {
                                    const img = await faceapi.fetchImage(`./src/labels/images/${label}/${i}.png`);
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
                                function handleDetection(result, labels) {
                                    if (result.label && labels.includes(result.label)) {
                                        const currentTime = new Date().getTime();
                                        const lastDetectionTime = localStorage.getItem("lastDetectionTime");
                                        if (!lastDetectionTime || currentTime - lastDetectionTime > 5000) {
                                            localStorage.setItem("lastDetectionTime", currentTime);
                                            const heading = document.createElement('h1');
                                            const text = document.createTextNode(`${result.label} detected at ${new Date().toLocaleTimeString()}`);
                                            heading.appendChild(text);
                                            document.getElementById('detection-log').appendChild(heading);
                                        }
                                    }
                                }


                                handleDetection(result, ["Messi", "Fiona", "Visard", "Ronaldo"]);
                            });
                        }, 100);
                    });
                },
                function (error) {
                    console.error(error)
                }
            )
        });

        return {

        };
    }
});
</script>
<style>
.notification {
    position: absolute;
    top: 10px;
    right: 10px;
    background-color: #fff;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.log {
    position: fixed;
    right: 0;
    top: 60px;
    width: 300px;
    background: rgba(255, 255, 255, 0.9);
    padding: 10px;
    height: 400px;
    overflow-y: auto;
}
</style>
