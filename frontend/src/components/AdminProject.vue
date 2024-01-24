<script setup lang="ts">
import { ref } from "vue";
import AdminImageInput from "@/components/AdminImageInput.vue";
const props = defineProps({
  auth: String,
});

const project = ref({
  title: "Project Title",
  subtitle: "Project Subtitle",
  description: "Project Description",
  img: "",
  button: {
    text: "Button Text",
    link: "/",
  },
});

const createProject = async () => {
  console.log(props.auth);
  await fetch(`${import.meta.env.VITE_API_URL}/projects/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Basic ${props.auth}`,
    },
    body: JSON.stringify(project.value),
  }).then((res) => {
    if (res.status !== 201) {
      alert("Error");
    }
  });
};
</script>

<template>
  <div class="mt-4 h-fit w-[600px] grow rounded-3xl bg-[#f3f4f6] px-4 py-6">
    <div class="flex">
      <AdminImageInput
        :auth="auth"
        id="project"
        @uploaded="
          (e) => {
            project.img = e;
          }
        "
      >
        <img
          height="70"
          width="70"
          alt=""
          class="h-[70px] w-[70px] cursor-pointer rounded"
          :src="project.img"
        />
      </AdminImageInput>
      <div class="ml-4 flex w-full flex-col justify-center font-semibold">
        <input
          class="rounded px-2 py-1 text-2xl text-[#0047FF]"
          type="text"
          placeholder="Project title"
          v-model="project.title"
        />
        <input
          class="mt-1 rounded px-2 py-1 text-sm text-gray-600"
          type="text"
          placeholder="Subtitle"
          v-model="project.subtitle"
        />
      </div>
    </div>
    <div class="mt-2 h-fit">
      <textarea
        class="h-40 w-full rounded px-2 py-1"
        placeholder="Description"
        v-model="project.description"
      ></textarea>
    </div>
    <div class="flex w-full flex-col items-center justify-center">
      <div
        class="mt-2 inline-block w-[70%] cursor-pointer rounded bg-[#0047FF] px-4 py-2"
      >
        <input
          class="w-full rounded px-2 py-1 font-semibold outline-none"
          type="text"
          placeholder="Button text"
          v-model="project.button.text"
        />
      </div>
      <input
        class="mt-2 w-full rounded bg-white px-2 py-1 text-lg"
        type="text"
        placeholder="Button url"
        v-model="project.button.link"
      />
    </div>
  </div>
  <button
    @click="createProject"
    class="mt-2 inline-block w-[600px] cursor-pointer rounded bg-[#0047FF] px-4 py-2 font-semibold text-white hover:brightness-125"
  >
    Create
  </button>
</template>
