import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state() {
    return {
      username: null,
      token: null,
    };
  },
  actions: {
    login(username, token) {
      this.username = username;
      this.token = token;
    },
    logout() {
      this.username = null;
      this.token = null;
    },
  },
});
