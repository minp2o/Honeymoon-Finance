<template>
  <div class="deposit-container">
    <h1>예금 상품 목록</h1>

    <div v-if="loading" class="loading-message">데이터를 불러오는 중입니다...</div>

    <div v-else-if="error" class="error-message">데이터를 불러오는 중 오류가 발생했습니다: {{ error }}</div>

    <div v-else-if="depositList.length > 0" class="deposit-list">
      <div v-for="(deposit, index) in depositList" :key="index" class="deposit-item">
        <h2>{{ deposit.kor_co_nm }} - {{ deposit.fin_prdt_nm }}</h2>
        <p><strong>가입 방법:</strong> {{ deposit.join_way }}</p>
        <p><strong>가입 제한:</strong> {{ deposit.join_deny === '1' ? '제한없음' : '제한있음' }}</p>
        <p><strong>가입 대상:</strong> {{ deposit.join_member }}</p>
        <p><strong>만기 후 이자율:</strong> {{ deposit.mtrt_int }}</p>
        <p><strong>우대 조건:</strong> {{ deposit.spcl_cnd }}</p>
        <p><strong>기타 유의사항:</strong> {{ deposit.etc_note }}</p>
      </div>
    </div>

    <div v-else class="no-data">
      <p>예금 상품을 찾을 수 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const deposits = ref(null)
const loading = ref(true)
const error = ref(null)

const depositList = ref([])

const fetchDepositData = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/fin_ins/deposit_list/')
    console.log('Fetched deposits:', response.data)
    depositList.value = response.data.result.baseList || []
  } catch (err) {
    error.value = err.message
    console.error('API 요청 오류:', err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchDepositData()
})
</script>

<style scoped>
.deposit-container {
  width: 80%;
  margin: 30px auto;
  padding: 20px;
  background-color: #f0f8ff;
  border-radius: 10px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #1e90ff;
  text-align: center;
  margin-bottom: 30px;
  font-size: 2.2em;
}

.loading-message,
.error-message,
.no-data {
  text-align: center;
  color: #4169e1;
  font-size: 1.2em;
  margin: 20px 0;
}

.deposit-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.deposit-item {
  background-color: #ffffff;
  border: 1px solid #87cefa;
  border-radius: 8px;
  padding: 15px;
  transition: transform 0.3s ease;
}

.deposit-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(30, 144, 255, 0.2);
}

.deposit-item h2 {
  color: #4169e1;
  font-size: 1.3em;
  margin-bottom: 10px;
  border-bottom: 2px solid #87cefa;
  padding-bottom: 5px;
}

.deposit-item p {
  margin: 8px 0;
  color: #333;
}

.deposit-item strong {
  color: #1e90ff;
}
</style>