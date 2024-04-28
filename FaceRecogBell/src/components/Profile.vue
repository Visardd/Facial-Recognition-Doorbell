<template>
  <div class="profile">
    <div class="profile-header">
      <img class="profile-picture" src="./Pic.png" alt="Profile Picture">
      <h1>{{ userStore.username }}</h1>
      <p>{{ userStore.email }}</p>
    </div>
    <div class="profile-content">
      <!-- Add additional profile information here -->
    </div>
  </div>
</template>

<script>
import { useUserStore } from '../stores/auth'
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {
    const userStore = useUserStore();

    return { userStore };
  }
})
</script>

<style>
.profile {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.profile-header {
  text-align: center;
}

.profile-picture {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
}

.profile h1 {
  font-size: 24px;
  margin-bottom: 5px;
}

.profile p {
  font-size: 16px;
  color: #888;
}


</style>
