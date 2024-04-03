<template>
  <header>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/LogIn">Log In!</RouterLink>
        <RouterLink to="/Signup">Signup</RouterLink>
        
      </nav>
  
  </header>

  <RouterView />
</template>
<script>
import { RouterLink, RouterView } from 'vue-router'
import { defineComponent } from "vue";
export default defineComponent({
  components: {
    RouterView,
  },
});
</script>
<style scoped>

</style>
