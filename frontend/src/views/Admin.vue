<script setup lang="ts">
import AdminProject from "@/components/AdminProject.vue";
import AdminPost from "@/components/AdminPost.vue";
import { ref, watch } from "vue";

const login = ref("");
const password = ref("");
const auth = ref("");
watch(
  [login, password],
  () => (auth.value = btoa(`${login.value}:${password.value}`)),
);
</script>

<template>
  <div class="px-6 py-4">
    <div class="flex flex-col items-center">
      <input
        class="w-[700px] rounded bg-[#F3F4F6] px-2 py-1 text-lg"
        type="text"
        placeholder="Login"
        v-model="login"
      />
      <input
        class="mt-2 w-[700px] rounded bg-[#F3F4F6] px-2 py-1 text-lg"
        type="text"
        placeholder="Password"
        v-model="password"
      />
    </div>
    <div class="mt-8 flex justify-around">
      <div>
        <AdminProject :auth="auth" />
      </div>
      <div>
        <AdminPost :auth="auth" />
      </div>
    </div>
  </div>
</template>

<style scoped></style>
