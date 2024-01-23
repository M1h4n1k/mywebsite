<script setup lang="ts">
import { useRoute } from "vue-router";
import { Post } from "@/types.ts";
import { onMounted, ref } from "vue";
import type { Ref } from "vue";

const fetchPost = async () => {
  const route = useRoute();
  return await fetch(
    `${import.meta.env.VITE_API_URL}/posts/${route.params._id}`,
  )
    .then((res) => res.json())
    .then((data) => {
      return data;
    });
};

let post: Ref<Post> = ref({} as Post);
onMounted(async () => {
  post.value = await fetchPost();
});
</script>

<template>
  <div class="flex w-full justify-center py-4">
    <div class="w-1/3 min-w-[300px]">
      <h1 class="text-3xl font-semibold">
        {{ post.title }}
      </h1>
      <img
        height="300px"
        width="100%"
        class="mt-2 h-[300px] w-full rounded-lg object-cover"
        :src="post.img"
        alt=""
      />
      <div class="mt-6" v-for="(b, i) of post.blocks" :key="i">
        <h3 class="text-xl font-semibold text-[#0047FF]">{{ b.title }}</h3>
        <p class="mt-2" v-for="(t, j) of b.text" :key="j">
          {{ t }}
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
