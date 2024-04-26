<template>
    <div class="profile-container">
      <div class="username-section">
        <h2>POggers</h2>
      </div>
      <div class="profile-image-section">
        <!-- <img :src="profileImage" alt="Profile Image" /> -->
        <button class="edit-button">Edit</button>
      </div>
      <div class="input-section">
        <label for="email" class="input-label">Email:</label>
        <!-- <input type="text" v-model="email" name="email"> -->
        <button class="save-button">Save</button>
      </div>
      <div class="input-section">
        <label for="dob" class="input-label">Date of Birth:</label>
        <!-- <input type="date" v-model="dob" name="dob"> -->
        <button class="save-button">Save</button>
      </div>
      <div class="favorite-category-section">
      <label for="favoriteCategory">Favorite Category:</label>
      <select name="favoriteCategory" id="favoriteCategory">
        <option value="Sports">Sports</option>
        <option value="Fashion">Fashion</option>
        <option value="Education">Education</option>
        <option value="Art">Art</option>
        <option value="World News">World News</option>
        <option value="Finance">Finance</option>
      </select>
      
    </div>
    </div>
  </template>
  