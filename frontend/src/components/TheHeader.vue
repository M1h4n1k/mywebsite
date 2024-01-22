<script setup lang="ts"></script>

<template>
  <header
    class="flex h-14 w-full items-center space-x-2 border-b px-[25%] text-xl font-semibold text-[#0047FF]"
  >
    <router-link
      to="/"
      :class="{
        'after:!h-1 after:!w-full': $route.path === '/',
      }"
    >
      Bio
    </router-link>
    <router-link
      to="/blog"
      :class="{
        'after:!h-1 after:!w-full': $route.path === '/blog',
      }"
    >
      Blog
    </router-link>
    <router-link
      to="/projects"
      :class="{
        'after:!h-1 after:!w-full': $route.path === '/projects',
      }"
    >
      Projects
    </router-link>
  </header>
</template>

<style scoped>
a {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 1rem;
  transition: border-bottom 300ms;
  position: relative;
}

a:hover::after {
  width: 100%;
  height: 4px;
}

a::after {
  content: "";
  position: absolute;
  bottom: 0;
  width: 0;
  height: 0;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  background-color: #0047ff;
  transition:
    width 200ms,
    height 200ms;
}
</style>
