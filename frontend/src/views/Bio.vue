<script setup lang="ts">
import BioEducation from "@/components/BioEducation.vue";
import BioITSkills from "@/components/BioITSkills.vue";
import BioAbout from "@/components/BioAbout.vue";
import BioContacts from "@/components/BioContacts.vue";
import BioWorkUnfairAdvantage from "@/components/BioWorkUnfairAdvantage.vue";
import BioWorkOther from "@/components/BioWorkOther.vue";
</script>

<template>
  <div class="flex w-full flex-col items-center px-6 py-5">
    <div class="!w-[992px] max-w-full space-y-4">
      <div class="flex items-end">
        <div class="h-28 w-28 min-w-28 rounded-lg bg-gray-300" />
        <h1 class="ml-4 w-fit text-4xl font-semibold text-[#0047FF]">
          Michael Karpow
        </h1>
      </div>
      <div class="flex flex-wrap gap-x-8 gap-y-6">
        <BioEducation />
        <BioITSkills />
      </div>
      <div class="flex flex-wrap gap-x-8 gap-y-6">
        <BioAbout />
        <BioContacts />
      </div>
      <h1 class="!mt-6 text-3xl font-semibold text-[#0047FF]">
        Working experience
      </h1>
      <div class="!mt-3 flex flex-wrap gap-x-8 gap-y-6">
        <BioWorkUnfairAdvantage />
        <BioWorkOther />
      </div>
    </div>
  </div>
</template>
