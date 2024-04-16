import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state() {
    return {
      username: null,
    };
  },
  actions: {
    login(username) {
      console.log("Username set!" + username)
      this.username = username;
    },
    logout() {
      this.username = null;
    },
  },
});
