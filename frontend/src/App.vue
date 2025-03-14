<script setup>
import { ref, onMounted } from 'vue';

const apiData = ref([]);

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/products/');  // Change this to match your API endpoint
    apiData.value = await response.json();
  } catch (error) {
    console.error('Error fetching API:', error);
  }
});
</script>

<template>
  <div>
    <h1>Products List</h1>
    <ul>
      <li v-for="item in apiData" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>
