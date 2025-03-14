<template>
    <div class="container mx-auto p-6">
      <h1 class="text-4xl font-extrabold text-indigo-700 text-center mb-8">Product Catalog</h1>
  
      <div v-if="loading" class="text-center text-gray-500">Loading products...</div>
  
      <div v-else-if="apiData.length === 0" class="text-center text-red-500">No products available</div>
  
      <div v-else class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
        <div v-for="item in apiData" :key="item.id" class="bg-white shadow-lg rounded-xl overflow-hidden p-5 transition-transform transform hover:scale-105">
          <img :src="item.image" class="w-full h-48 object-cover rounded-lg">
          
          <div class="mt-4">
            <h2 class="text-xl font-semibold text-gray-900">{{ item.name }}</h2>
            <p class="text-gray-600 text-sm mt-1">{{ item.description }}</p>
            <p class="text-green-500 font-bold text-lg mt-2">${{ item.price }}</p>
            
            <button class="mt-3 w-full bg-indigo-600 text-white py-2 rounded-lg hover:bg-indigo-500 transition">
              View Details
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  const apiData = ref([]);
  const loading = ref(true);
  
  onMounted(async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/products/');
      apiData.value = await response.json();
    } catch (error) {
      console.error('Error fetching API:', error);
    } finally {
      loading.value = false;
    }
  });
  </script>
  
  <style>
  body {
    background: linear-gradient(to right, #ece9e6, #ffffff);
  }
  </style>
  