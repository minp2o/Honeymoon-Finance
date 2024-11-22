<template>
    <div>
      <h1>예금 상품 정보</h1>
      <div v-if="loading">로딩 중...</div>
      <div v-else>
        <h2>기본 상품 목록</h2>
        <ul>
          <li v-for="item in baseList" :key="item.fin_prdt_cd">
            {{ item.fin_prdt_nm }} - {{ item.kor_co_nm }} (가입 제한: {{ item.join_deny }})
          </li>
        </ul>
        <h2>옵션 목록</h2>
        <ul>
          <li v-for="option in optionList" :key="option.fin_prdt_cd">
            {{ option.intr_rate_type_nm }} - 금리: {{ option.intr_rate }}%
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        baseList: [],
        optionList: [],
        loading: true,
      };
    },
    mounted() {
      this.fetchDepositData();
    },
    methods: {
      async fetchDepositData() {
        try {
          const response = await fetch('http://localhost:5173/compare');
          const data = await response.json();
          this.baseList = data.baseList;
          this.optionList = data.optionList;
        } catch (error) {
          console.error('데이터를 가져오는 중 오류 발생:', error);
        } finally {
          this.loading = false;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* 스타일을 추가할 수 있습니다. */
  </style>