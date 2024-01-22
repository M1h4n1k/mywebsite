<script setup lang="ts">
const posts = [
  {
    _id: "1",
    img: "https://picsum.photos/seed/1/1080/200",
    title: "Some name",
    caption:
      "In tempor pulvinar sollicitudin. In hac habitasse platea dictumst. " +
      "In non aliquam nulla. Cras arcu tellus, lobortis condimentum justo id," +
      " posuere finibus nibh. Mauris quis justo ligula. Praesent sit amet urna" +
      " sed lacus gravida pretium. Fusce ac mi non nulla faucibus tempus a ac ex." +
      " Vestibulum lacinia, risus vitae interdum commodo, metus neque posuere nisl," +
      " maximus condimentum metus risus id felis. ",
    link: "/blog/1",
  },
  {
    _id: "2",
    img: "https://picsum.photos/seed/2/1080/200",
    title: "Some name 2",
    caption:
      "In tempor pulvinar sollicitudin. In hac habitasse platea dictumst. " +
      "In non aliquam nulla. Cras arcu tellus, lobortis condimentum justo id," +
      " posuere finibus nibh. Mauris quis justo ligula. Praesent sit amet urna" +
      " sed lacus gravida pretium. Fusce ac mi non nulla faucibus tempus a ac ex." +
      " Vestibulum lacinia, risus vitae interdum commodo, metus neque posuere nisl," +
      " maximus condimentum metus risus id felis. ",
    link: "/blog/2",
  },
];
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
          :to="post.link"
        >
          Read more
        </router-link>
      </div>
    </div>
  </div>
</template>
