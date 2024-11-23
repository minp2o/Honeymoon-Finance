import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router' // 라우터 파일을 import

export const useCounterStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => !!token.value)

  // Axios 인스턴스 생성
  const apiClient = axios.create({
    baseURL: API_URL,
  })

  // Axios 응답 인터셉터 추가
  apiClient.interceptors.response.use(
    response => response,
    error => {
      if (error.response && error.response.status === 401) {
        // 401 Unauthorized 오류 발생 시 토큰을 삭제하고 로그인 페이지로 리다이렉트
        console.error('토큰이 만료되었습니다. 로그아웃 처리 중...')
        token.value = null // 토큰 삭제
        router.push({ name: 'LogInView' }) // 로그인 페이지로 리다이렉트
        alert('세션이 만료되었습니다. 다시 로그인해주세요.')
      }
      return Promise.reject(error)
    }
  )

  // 로그인 함수 정의
  const logIn = function (payload) {
    return apiClient({
      method: 'post',
      url: `/dj-rest-auth/login/`,
      data: payload,
    })
      .then((res) => {
        token.value = res.data.key
        return res
      })
      .catch((err) => {
        console.error('로그인 실패:', err)
        throw err
      })
  }

  // 회원가입 함수
  const signUp = function (payload) {
    const { username, password1, password2, nickname, email, age, gender, phone } = payload

    if (password1 !== password2) {
      console.error('비밀번호가 서로 다릅니다.')
      alert('비밀번호가 서로 다릅니다!')
      return Promise.reject(new Error('비밀번호 불일치'))
    }

    return apiClient({
      method: 'post',
      url: `/dj-rest-auth/registration/`,
      data: {
        username, password1, password2, nickname, email, age, gender, phone,
      },
    })
      .then((res) => {
        console.log('회원가입 성공:', res)
        router.push({ name: 'LogInView' })
      })
      .catch((err) => {
        console.error('회원가입 실패:', err.response ? err.response.data : err.message)
        throw err
      })
  }

  // 로그아웃 함수 정의
  const logOut = function () {
    if (!token.value) {
      console.error('로그아웃 실패: 유효하지 않은 토큰입니다.')
      alert('유효하지 않은 토큰으로 로그아웃을 시도했습니다.')
      return Promise.reject(new Error('로그아웃 실패: 유효하지 않은 토큰'))
    }

    return apiClient({
      method: 'post',
      url: `/dj-rest-auth/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(() => {
        console.log('로그아웃 성공')
        token.value = null
        router.push({ name: 'HomeView' })
      })
      .catch((err) => {
        console.error('로그아웃 실패:', err.response ? err.response.data : err.message)
        if (err.response && err.response.status === 401) {
          alert('로그아웃에 실패했습니다. 이미 만료된 토큰입니다.')
        }
        throw err
      })
  }

  return { API_URL, signUp, logIn, logOut, token, isLogin }
}, { persist: true })
