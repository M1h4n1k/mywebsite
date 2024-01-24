<script setup lang="ts">
const emit = defineEmits(["uploaded"]);
const props = defineProps({
  auth: String,
  id: String,
});

const uploadImage = (e: Event) => {
  const target = e.target as HTMLInputElement;
  const file = target.files ? target.files[0] : null;
  if (!file) {
    alert("Error, no image");
    return;
  }
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = () => {
    const formData = new FormData();
    formData.append("file", file);
    fetch(`${import.meta.env.VITE_API_URL}/upload`, {
      method: "POST",
      headers: {
        Authorization: `Basic ${props.auth}`,
      },
      body: formData,
    })
      .then((response) => response.json())
      .then((res) => {
        emit(
          "uploaded",
          import.meta.env.VITE_API_URL.replace("/api", "") + res,
        );
      })
      .catch((error) => console.log(error));
  };
};
</script>

<template>
  <div>
    <label :for="id">
      <slot></slot>
    </label>
    <input
      :id="id"
      type="file"
      accept="image/jpeg"
      class=""
      style="opacity: 0; position: absolute; z-index: -1"
      @change="uploadImage"
    />
  </div>
</template>
