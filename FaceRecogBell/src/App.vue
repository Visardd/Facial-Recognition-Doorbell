<template>
  <header>
  <navbar1 />
  
  </header>

  <RouterView />
</template>
<script>
import { RouterLink, RouterView } from 'vue-router'
import { defineComponent } from "vue";
import navbar1 from '@/components/navbar1.vue';
export default defineComponent({
  components: {
    RouterView,
    navbar1
  },
});
</script>
<style scoped>

</style>
