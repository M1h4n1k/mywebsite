<script setup lang="ts">
import { ref } from "vue";
import AdminImageInput from "@/components/AdminImageInput.vue";

const props = defineProps({
  auth: String,
});

let post = ref({
  title: "",
  img: "",
  caption: "",
  blocks: [
    {
      title: "",
      text: [""],
    },
  ],
});

const createPost = async () => {
  await fetch(`${import.meta.env.VITE_API_URL}/posts/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Basic ${props.auth}`,
    },
    body: JSON.stringify(post.value),
  }).then((res) => {
    if (res.status !== 201) {
      alert("Error");
      return;
    }
    alert("Success");
  });
};
</script>

<template>
  <div class="mt-4 w-[700px]">
    <input
      class="w-full rounded bg-[#F3F4F6] px-2 py-1 text-3xl font-semibold"
      type="text"
      placeholder="Post title"
      v-model="post.title"
    />

    <AdminImageInput
      :auth="auth"
      id="post"
      @uploaded="
        (e) => {
          post.img = e;
        }
      "
    >
      <img
        height="300px"
        width="100%"
        class="mt-2 h-[300px] w-full cursor-pointer rounded-lg object-cover"
        :src="post.img"
        alt=""
      />
    </AdminImageInput>
    <textarea
      class="mt-2 h-28 w-full rounded bg-[#F3F4F6] px-2 py-1"
      placeholder="Caption"
      v-model="post.caption"
    ></textarea>
    <div class="relative mt-6" v-for="(b, i) of post.blocks" :key="i">
      <button
        @click="post.blocks.splice(i, 1)"
        class="absolute -left-10 top-1 h-8 w-8 rounded-full bg-red-500 text-lg font-extrabold text-white hover:brightness-125"
      >
        &#8212;
      </button>
      <input
        class="rounded bg-[#F3F4F6] px-2 py-1 text-xl font-semibold text-[#0047FF]"
        type="text"
        placeholder="Block title"
        v-model="post.blocks[i].title"
      />
      <div class="relative" v-for="(t, j) of b.text" :key="j">
        <button
          @click="
            () => {
              console.log(post.blocks[i].text[j]);
              post.blocks[i].text.splice(j, 1);
            }
          "
          class="absolute -left-8 top-2 h-6 w-6 rounded-full bg-red-500 text-xs font-bold text-white hover:brightness-125"
        >
          &#8212;
        </button>
        <textarea
          class="mt-2 h-20 w-full rounded bg-[#F3F4F6] px-2 py-1"
          placeholder="Description"
          v-model="post.blocks[i].text[j]"
        ></textarea>
      </div>
      <button
        class="mt-2 inline-block w-64 cursor-pointer rounded bg-[#0047FF] px-4 py-1 text-xs font-semibold text-white hover:brightness-125"
        @click="post.blocks[i].text.push('')"
      >
        Add paragraph
      </button>
    </div>
    <button
      @click="post.blocks.push({ title: '', text: [''] })"
      class="mt-4 inline-block w-80 cursor-pointer rounded bg-[#0047FF] px-4 py-2 text-sm font-semibold text-white hover:brightness-125"
    >
      Add block
    </button>
  </div>
  <button
    @click="createPost"
    class="mt-8 inline-block w-[700px] cursor-pointer rounded bg-[#0047FF] px-4 py-2 font-semibold text-white hover:brightness-125"
  >
    Publish
  </button>
</template>

<style scoped></style>
