<template>
  <div>
    <h1>Hello {{ userStore.username }}</h1>
    <input type="file" @change="onFileChange">
    <input type="text" v-model="category" placeholder="Enter category">
    <button @click="uploadImage">Upload Image</button>
    <div v-if="uploadSuccess" class="alert alert-success mt-3">File uploaded successfully!</div>
    <div v-if="imagePreview">
      <h3>Image Preview:</h3>
      <img :src="imagePreview" alt="Preview" width="200">
    </div>
  </div>
</template>

<script>

import axios from 'axios';
import { useUserStore } from '../stores/auth'
import { defineComponent } from 'vue'


export default defineComponent({
  data() {
    return {
      image: null,
      category: '',
      uploadSuccess: false,
      imagePreview: null,
    }
  },
  setup() {
		const userStore = useUserStore();

		return { userStore };
	},
  methods: {
    onFileChange(e) {
      this.image = e.target.files[0];
      this.imagePreview = URL.createObjectURL(this.image); // Create a preview URL for the selected image
    },
    uploadImage() {
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
    }
  }
})
</script>

<style>
input[type="file"],
input[type="text"],
button {
  margin: 10px;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.alert {
  padding: 10px;
  background-color: #dff0d8;
  border: 1px solid #d6e9c6;
  border-radius: 4px;
  color: #3c763d;
}
</style>
