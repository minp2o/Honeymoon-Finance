import axios from 'axios';

// const instance = axios.create({
//   baseURL: '/api',  // vue.config.js의 프록시 설정과 일치
//   withCredentials: true  // 자격 증명 포함
// });

// export default instance;

const api = axios.create({
    baseURL: 'http://localhost:5174/api/'
  })
  
  export default {
    getFinancialProducts() {
      return api.get('products/')
    },
    getFinancialProduct(id) {
      return api.get(`products/${id}/`)
    }
    // 필요한 다른 API 호출 메서드들을 여기에 추가할 수 있습니다.
  }