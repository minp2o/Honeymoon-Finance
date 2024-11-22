<template>
    <div class="main-page">
      <h1>금융 상품 추천</h1>
      <div class="product-list">
        <div v-for="product in products" :key="product.id" class="product-item">
          <h2>{{ product.name }}</h2>
          <p>{{ product.description }}</p>
          <p>이자율: {{ product.interest_rate }}%</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'MainPage',
    data() {
      return {
        products: []
      }
    },
    mounted() {
      this.fetchProducts();
    },
    methods: {
      async fetchProducts() {
        try {
          const response = await axios.get('http://localhost:5174/api/products/');
          this.products = response.data;
        } catch (error) {
          console.error('상품을 불러오는 데 실패했습니다:', error);
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .main-page {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .product-item {
    border: 1px solid #ddd;
    padding: 10px;
    margin-bottom: 10px;
  }
  </style>