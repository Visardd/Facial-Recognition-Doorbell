<template>
    <div>
      <input type="file" @change="onFileChange">
      <input type="text" v-model="category" placeholder="Enter category">
      <button @click="uploadImage">Upload Image</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        image: null,
        category: '',
      }
    },
    methods: {
      onFileChange(e) {
        this.image = e.target.files[0];
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
        .then(response => console.log(response))
        .catch(error => console.error(error));
      }
    }
  }
  </script>
  