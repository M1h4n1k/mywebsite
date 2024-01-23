<script lang="ts" setup>
import { Post } from "@/types.ts";
import { onMounted, ref } from "vue";
import type { Ref } from "vue";

let posts: Ref<Post[]> = ref([]);
const fetchPosts = async () => {
  return await fetch(`${import.meta.env.VITE_API_URL}/posts/`)
    .then((res) => res.json())
    .then((data) => {
      return data;
    });
};
onMounted(async () => {
  posts.value = await fetchPosts();
});
</script>

<template>
  <div class="flex w-full flex-col flex-wrap items-center gap-8 px-6 py-8">
    <div
      class="h-fit w-1/2 rounded-3xl bg-[#f3f4f6] px-4 py-5"
      v-for="post of posts"
      :key="post._id"
    >
      <h2 class="text-2xl font-semibold text-[#0047FF]">
        {{ post.title }}
      </h2>
      <img
        height="200"
        alt=""
        class="my-2 h-[200px] w-full rounded-lg"
        :src="post.img"
      />
      <div class="h-fit">
        {{ post.caption }}
      </div>
      <div class="mt-2 flex w-full justify-end">
        <router-link
          class="mt-2 inline-block w-[150px] cursor-pointer rounded bg-[#0047FF] px-4 py-2 text-center font-semibold text-white hover:brightness-125"
          :to="'/blog/' + post._id"
        >
          Read more
        </router-link>
      </div>
    </div>
  </div>
</template>
