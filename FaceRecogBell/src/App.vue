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
import navbar2 from '@/components/navbar2.vue';
import { useUserStore } from '../src/stores/auth'
export default defineComponent({
  components: {
    RouterView,
    navbar1,
    navbar2
  },
  setup(){
          const userStore = useUserStore();
          return { userStore };
        }
});
</script>
<style scoped>

</style>
