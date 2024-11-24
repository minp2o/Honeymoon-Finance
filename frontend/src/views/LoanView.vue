<template>
    <div class="loan-container">
      <h1>전세자금대출 상품 목록</h1>
  
      <div v-if="loading" class="loading-message">데이터를 불러오는 중입니다...</div>
  
      <div v-else-if="error" class="error-message">데이터를 불러오는 중 오류가 발생했습니다: {{ error }}</div>
  
      <div v-else-if="loanList.length > 0" class="loan-list">
        <div v-for="(loan, index) in loanList" :key="index" class="loan-item">
          <h2>{{ loan.kor_co_nm }} - {{ loan.fin_prdt_nm }}</h2>
          <p><strong>대출 한도:</strong> {{ loan.loan_lmt }}</p>
          <p><strong>가입 방법:</strong> {{ loan.join_way }}</p>
          <p><strong>중도 상환 수수료:</strong> {{ loan.erly_rpay_fee }}</p>
          <p><strong>연체 이자율:</strong> {{ loan.dly_rate }}</p>
  
          <div class="loan-options">
            <h3>대출 옵션</h3>
            <div v-for="(option, idx) in getLoanOptions(loan.fin_prdt_cd)" :key="idx" class="loan-option-item">
              <p><strong>상환 방식:</strong> {{ option.rpay_type_nm }}</p>
              <p><strong>금리 유형:</strong> {{ option.lend_rate_type_nm }}</p>
              <p><strong>최소 금리:</strong> {{ option.lend_rate_min }}%</p>
              <p><strong>최대 금리:</strong> {{ option.lend_rate_max }}%</p>
              <p><strong>평균 금리:</strong> {{ option.lend_rate_avg }}%</p>
            </div>
          </div>
        </div>
      </div>
  
      <div v-else class="no-data">
        <p>전세자금대출 상품을 찾을 수 없습니다.</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue'
  import axios from 'axios'
  
  const loans = ref(null)
  const loading = ref(true)
  const error = ref(null)
  
  const loanList = computed(() => loans.value?.result?.baseList || [])
  const loanOptions = computed(() => loans.value?.result?.optionList || [])
  
  const getLoanOptions = (finPrdtCd) => {
    return loanOptions.value.filter(option => option.fin_prdt_cd === finPrdtCd)
  }
  
  const fetchLoanData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/loan/')
      console.log('Fetched loans:', response.data)
      loans.value = response.data
    } catch (err) {
      error.value = err.message
      console.error('API 요청 오류:', err)
    } finally {
      loading.value = false
    }
  }
  
  onMounted(() => {
    fetchLoanData()
  })
  </script>

<style scoped>
.loan-container {
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

.loan-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.loan-item {
  background-color: #ffffff;
  border: 1px solid #87cefa;
  border-radius: 8px;
  padding: 15px;
  transition: transform 0.3s ease;
}

.loan-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(30, 144, 255, 0.2);
}

.loan-item h2 {
  color: #4169e1;
  font-size: 1.3em;
  margin-bottom: 10px;
  border-bottom: 2px solid #87cefa;
  padding-bottom: 5px;
}

.loan-item p {
  margin: 8px 0;
  color: #333;
}

.loan-item strong {
  color: #1e90ff;
}

.loan-options {
  background-color: #e6f3ff;
  border-radius: 5px;
  padding: 10px;
  margin-top: 15px;
}

.loan-options h3 {
  color: #4169e1;
  font-size: 1.1em;
  margin-bottom: 10px;
}

.loan-option-item {
  border-bottom: 1px solid #b0e0e6;
  padding-bottom: 8px;
  margin-bottom: 8px;
}

.loan-option-item:last-child {
  border-bottom: none;
}
</style>