<script setup lang="ts">
const projects = [
  {
    _id: "1",
    img: "https://picsum.photos/seed/1/300/300",
    title: "Some name",
    subtitle: "Some subtitle",
    description:
      "In tempor pulvinar sollicitudin. In hac habitasse platea dictumst. " +
      "In non aliquam nulla. Cras arcu tellus, lobortis condimentum justo id," +
      " posuere finibus nibh. Mauris quis justo ligula. Praesent sit amet urna" +
      " sed lacus gravida pretium. Fusce ac mi non nulla faucibus tempus a ac ex." +
      " Vestibulum lacinia, risus vitae interdum commodo, metus neque posuere nisl," +
      " maximus condimentum metus risus id felis. ",
    button: {
      text: "Read more",
      link: "https://goo.gle",
    },
  },
  {
    _id: "2",
    img: "https://picsum.photos/seed/2/300/300",
    title: "Some name 2",
    subtitle: "Some subtitle 2",
    description:
      "In tempor pulvinar sollicitudin. In hac habitasse platea dictumst. " +
      "In non aliquam nulla. Cras arcu tellus, lobortis condimentum justo id," +
      " posuere finibus nibh. Mauris quis justo ligula. Praesent sit amet urna" +
      " sed lacus gravida pretium. Fusce ac mi non nulla faucibus tempus a ac ex." +
      " Vestibulum lacinia, risus vitae interdum commodo, metus neque posuere nisl," +
      " maximus condimentum metus risus id felis. ",
    button: {
      text: "Read more",
      link: "https://goo.gle",
    },
  },
];
</script>

<template>
  <div class="flex w-full flex-wrap gap-4 px-6 py-4">
    <div
      class="h-fit w-1/3 min-w-[300px] max-w-[600px] grow rounded-3xl bg-[#f3f4f6] px-4 py-6"
      v-for="project of projects"
      :key="project._id"
    >
      <div class="flex">
        <img height="70" width="70" alt="" class="rounded" :src="project.img" />
        <div class="ml-4 flex w-full flex-col justify-center font-semibold">
          <h2 class="text-2xl text-[#0047FF]">
            {{ project.title }}
          </h2>
          <h6 class="text-sm text-gray-500">
            {{ project.subtitle }}
          </h6>
        </div>
      </div>
      <div class="mt-2 h-fit">
        {{ project.description }}
      </div>
      <div class="flex w-full justify-center">
        <component
          :is="project.button.link.startsWith('http') ? 'a' : 'router-link'"
          class="mt-2 inline-block w-[70%] cursor-pointer rounded bg-[#0047FF] px-4 py-2 text-center font-semibold text-white hover:brightness-125"
          :to="project.button.link"
          :href="project.button.link"
          target="_blank"
        >
          {{ project.button.text }}
        </component>
      </div>
    </div>
  </div>
</template>
