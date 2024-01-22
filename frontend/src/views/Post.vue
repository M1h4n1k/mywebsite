<script setup lang="ts">
import { useRoute } from "vue-router";
const route = useRoute();

const post = {
  _id: route.params._id,
  img: "https://picsum.photos/seed/123/700/300",
  title: "How I was writing my own website",
  blocks: [
    {
      title: "Introduction",
      text: [
        "Nullam commodo nisi ac laoreet commodo. Fusce laoreet vitae odio dignissim laoreet. Morbi vitae magna ipsum. Quisque nec ipsum efficitur, sodales ex quis, malesuada metus. Morbi porttitor pellentesque fringilla. Cras varius erat ac risus dignissim laoreet. Maecenas et sollicitudin enim, at lacinia turpis",
        "Aliquam vitae est aliquam, mattis enim ut, porttitor augue. Cras enim enim, ultrices eu tortor at, posuere dapibus dolor. Vestibulum fermentum commodo convallis. Suspendisse felis ligula, condimentum eu diam eget, pellentesque venenatis turpis.",
      ],
    },
    {
      title: "Explanation",
      text: [
        "Aenean sit amet facilisis nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Mauris vulputate odio id dui consectetur, nec dictum neque tempor. Proin imperdiet, sem sit amet accumsan dignissim, enim lectus consequat ipsum, vel rutrum justo purus quis mauris. Aenean tincidunt, eros hendrerit efficitur vestibulum, dui risus imperdiet felis, a fringilla sapien erat sodales erat. Proin suscipit odio purus, sed dictum tortor tincidunt id. Ut blandit velit eu odio malesuada porta. Nulla vestibulum ullamcorper tempor. Duis convallis ut ipsum non ultricies. Aenean sit amet tortor tortor. Fusce lacus turpis, blandit at interdum nec, sagittis et arcu. ",
        "Aenean neque erat, porttitor non finibus at, dignissim vitae urna. Curabitur sed blandit odio, a laoreet lectus. Cras a justo nec augue dapibus malesuada vel at risus. Vivamus in arcu fermentum, mollis tortor et, aliquet nisi. Maecenas ultrices, dolor eu feugiat sollicitudin, dolor lorem gravida neque, non lacinia velit nisi volutpat augue. Proin blandit, lorem sed viverra rutrum, neque felis scelerisque nisl, ac imperdiet nisi purus nec augue. Donec quis sodales lorem. Proin tempus lectus nec enim eleifend condimentum. Nullam leo mi, tempus at lacus sit amet, placerat dignissim risus. Praesent ex neque, dapibus vitae orci ut, varius consectetur ante. Nam iaculis blandit eros at porttitor. Nullam quam metus, tincidunt elementum velit sit amet, vulputate sollicitudin ipsum. Proin efficitur, neque ac luctus semper, est risus porta mauris, non semper ex lacus non mi. Nulla maximus risus et metus lacinia gravida sed eu enim. Praesent et pulvinar quam. Suspendisse et augue vehicula, euismod sem semper, vestibulum lacus. ",
      ],
    },
  ],
};
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
