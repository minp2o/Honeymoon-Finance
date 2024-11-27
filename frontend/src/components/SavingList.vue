<template>
  <div class="saving-container">
    <h1>적금 상품 목록</h1>
    <h4 id="period">저축 기간</h4>

    <div class="sorting-buttons">
      <button v-for="period in savingPeriods" :key="period" @click="sortBySavingPeriod(period)">
        {{ period }}개월
      </button>
    </div>

    <div v-if="loading" class="loading-message">데이터를 불러오는 중입니다...</div>

    <div v-else-if="error" class="error-message">데이터를 불러오는 중 오류가 발생했습니다: {{ error }}</div>

    <div v-else-if="filteredSavingList.length > 0" class="saving-list">
      <div v-for="(saving, index) in filteredSavingList" :key="index" class="saving-item">
        <h2>{{ saving.kor_co_nm }} - {{ saving.fin_prdt_nm }}</h2>
        <p><strong>가입 방법:</strong> {{ saving.join_way }}</p>
        <p><strong>가입 제한:</strong> {{ saving.join_deny }}</p>
        <p><strong>가입 대상:</strong> {{ saving.join_member }}</p>
        <p><strong>기타 유의사항:</strong> {{ saving.etc_note }}</p>
        <p><strong>만기 후 이자율:</strong> {{ saving.mtrt_int }}</p>
        <p><strong>특별 조건:</strong> {{ saving.spcl_cnd }}</p>

        <div class="saving-options">
          <h3>적금 옵션</h3>
          <div v-for="(option, idx) in getSavingOptions(saving.fin_prdt_cd)" :key="idx" class="saving-option-item">
            <p><strong>저축 기간:</strong> {{ option.save_trm }}</p>
            <p><strong>적립 유형:</strong> {{ option.rsrv_type_nm }}</p>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="no-data">
      <p>적금 상품을 찾을 수 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

const savings = ref(null)
const loading = ref(true)
const error = ref(null)
const selectedPeriod = ref(null)

const savingPeriods = [6, 12, 18, 24, 30, 36]

const savingList = computed(() => savings.value?.result?.baseList || [])
const savingOptions = computed(() => savings.value?.result?.optionList || [])

const filteredSavingList = computed(() => {
  if (!selectedPeriod.value) return savingList.value
  return savingList.value.filter(saving => {
    const options = getSavingOptions(saving.fin_prdt_cd)
    return options.some(option => parseInt(option.save_trm) === selectedPeriod.value)
  })
})

const getSavingOptions = (finPrdtCd) => {
  return savingOptions.value.filter(option => option.fin_prdt_cd === finPrdtCd)
}

const sortBySavingPeriod = (period) => {
  selectedPeriod.value = period
}

const fetchSavingData = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/fin_ins/saving_list/')
    console.log('Fetched savings:', response.data)
    savings.value = response.data
  } catch (err) {
    error.value = err.message
    console.error('API 요청 오류:', err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchSavingData()
})
</script>

<style scoped>
#period{
  text-align: center;
  padding-bottom: 10px;
  color: #1e90ff;
  
}

.saving-container {
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

.saving-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.saving-item {
  background-color: #ffffff;
  border: 1px solid #87cefa;
  border-radius: 8px;
  padding: 15px;
  transition: transform 0.3s ease;
}

.saving-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(30, 144, 255, 0.2);
}

.saving-item h2 {
  color: #4169e1;
  font-size: 1.3em;
  margin-bottom: 10px;
  border-bottom: 2px solid #87cefa;
  padding-bottom: 5px;
}

.saving-item p {
  margin: 8px 0;
  color: #333;
}

.saving-item strong {
  color: #1e90ff;
}

.saving-options {
  background-color: #e6f3ff;
  border-radius: 5px;
  padding: 10px;
  margin-top: 15px;
}

.saving-options h3 {
  color: #4169e1;
  font-size: 1.1em;
  margin-bottom: 10px;
}

.saving-option-item {
  border-bottom: 1px solid #b0e0e6;
  padding-bottom: 8px;
  margin-bottom: 8px;
}

.saving-option-item:last-child {
  border-bottom: none;
}

.sorting-buttons {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.sorting-buttons button {
  background-color: #4169e1;
  color: white;
  border: none;
  padding: 10px 15px;
  margin: 0 5px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.sorting-buttons button:hover {
  background-color: #1e90ff;
}
</style>