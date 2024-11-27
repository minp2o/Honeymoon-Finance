<template>
    <div class="survey-container">
      <h1>금융 설문조사</h1>
      <form @submit.prevent="submitSurvey">
        <div class="form-group">
          <label>자동차를 소유하고 계십니까?</label>
          <div class="radio-group">
            <label><input type="radio" v-model="surveyData.has_car" :value="true"> 예</label>
            <label><input type="radio" v-model="surveyData.has_car" :value="false"> 아니오</label>
          </div>
        </div>
  
        <div class="form-group">
          <label>주택을 소유하고 계십니까?</label>
          <div class="radio-group">
            <label><input type="radio" v-model="surveyData.has_home" :value="true"> 예</label>
            <label><input type="radio" v-model="surveyData.has_home" :value="false"> 아니오</label>
          </div>
        </div>
  
        <div class="form-group">
          <label>재산 (단위: 원)</label>
          <input type="number" v-model.number="surveyData.property" min="0">
        </div>
  
        <div class="form-group">
          <label>연간 소득 (단위: 원)</label>
          <input type="number" v-model.number="surveyData.income" min="0">
        </div>
  
        <div class="form-group">
          <label>수도권 거주 계획이십니까?</label>
          <div class="radio-group">
            <label><input type="radio" v-model="surveyData.in_seoul" :value="true"> 예</label>
            <label><input type="radio" v-model="surveyData.in_seoul" :value="false"> 아니오</label>
          </div>
        </div>
  
        <div class="form-group">
          <label>3년 이내 자녀 계획이 있으십니까?</label>
          <div class="radio-group">
            <label><input type="radio" v-model="surveyData.children" :value="true"> 예</label>
            <label><input type="radio" v-model="surveyData.children" :value="false"> 아니오</label>
          </div>
        </div>
  
        <div class="form-group">
          <label>예산 (단위: 원)</label>
          <input type="number" v-model.number="surveyData.budget" min="0">
        </div>
  
        <button type="submit" class="submit-btn">제출하기</button>
      </form>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useCounterStore } from '@/stores/counter'
  import { useRouter } from 'vue-router'

  
  export default {
    setup() {
      const router = useRouter()
      const store = useCounterStore()
      const surveyData = ref({
        has_car: null,
        has_home: null,
        property: 0,
        income: 0,
        in_seoul: null,
        children: null,
        budget: 0
      })
  
      const submitSurvey = async () => {
        try {
          const response = await axios.put('http://127.0.0.1:8000/accounts/survey/', surveyData.value, {
            headers: {
              Authorization: `Token ${store.token}`
            }
          })
          console.log('Survey submitted successfully:', response.data)
          alert('설문조사가 성공적으로 제출되었습니다.')
            router.push({ name: 'HomeView' }) 
        } catch (error) {
          console.error('Error submitting survey:', error)
          alert('설문조사 제출 중 오류가 발생했습니다.')
        }
      }
  
      return {
        surveyData,
        submitSurvey
      }
    }
  }
  </script>
  
  <style scoped>
  .survey-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }
  
  h1 {
    text-align: center;
    color: #333;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  .radio-group {
    display: flex;
    gap: 20px;
  }
  
  .radio-group label {
    display: inline-flex;
    align-items: center;
  }
  
  input[type="number"] {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  .submit-btn {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .submit-btn:hover {
    background-color: #45a049;
  }
  </style>