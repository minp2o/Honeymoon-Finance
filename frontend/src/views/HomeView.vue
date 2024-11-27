<script setup>

// 필요한 경우 여기에 추가 스크립트
</script>
<template>
  <div class="home">
    <div class="background-image">
    <h1 class="title">신혼부부를 위한 금융 상품 추천</h1>
    <div class="honeymoon-finance">Honeymoon Finance</div>
      
    </div>
    <div class="main-content">

    </div>
  </div>
</template>




<style scoped>
.honeymoon-finance {
  font-family: 'Brush Script MT', cursive;
  font-size: 6rem;
  color: #ffffff;
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  z-index: 1;
}

.home {
  position: relative;
  min-height: 100vh;
}

.title {
  font-size: 2rem;
  margin-bottom: 2.5rem;
  color: #2c3e50;
  font-weight: bold;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 2px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  font-family: 'Arial', sans-serif;
  position: relative;
  padding-bottom: 15px;
}

.title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 4px;
  background-color: #3498db;
  border-radius: 2px;
}

.main-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

.main-image {
  height: 100%;
  width: 100%;
  
  
}

.action-button {
  display: inline-block;
  padding: 1rem 2rem;
  background-color: #666;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-size: 1.2rem;
  transition: background-color 0.3s;
}

.image-container {
  position: fixed;
  padding-top: 80px;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  object-fit: cover;
}

.action-button:hover {
  background-color: #444;
}

.background-image {
  position: absolute;
  top: 20px; /* nav바 높이 */
  left: 0;
  right: 0;
  bottom: 0;
  background-image: linear-gradient(to top, rgba(255,255,255,0) 0%, rgba(255,255,255,0.8) 100%),url('@/assets/WEDDING2.jpg');
  background-size: cover;
  background-position: center;
  z-index: -1;
}

</style>