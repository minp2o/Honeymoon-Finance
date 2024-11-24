<template>
  <div class="login-container">
    <h1>로그인</h1>
    <form @submit.prevent="logIn" class="login-form">
      <div class="form-group">
        <label for="username">username:</label>
        <input type="text" id="username" v-model.trim="username" required>
      </div>

      <div class="form-group">
        <label for="password">password:</label>
        <input type="password" id="password" v-model.trim="password" required>
      </div>

      <input type="submit" value="로그인" class="login-button">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const username = ref(null)
const password = ref(null)

const store = useCounterStore()
const router = useRouter()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
    .then(() => {
      router.push({ name: 'HomeView' })
    })
    .catch((err) => {
      if (err.response) {
        console.error('로그인 실패 - 상태 코드:', err.response.status, '메시지:', err.response.data)
        alert('로그인에 실패했습니다. 아이디와 비밀번호를 확인하세요.')
      } else if (err.request) {
        console.error('로그인 실패 - 요청은 보내졌으나 응답이 없습니다:', err.request)
        alert('서버로부터 응답을 받지 못했습니다. 네트워크를 확인하세요.')
      } else {
        console.error('로그인 실패 - 오류 메시지:', err.message)
        alert('로그인 요청 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.')
      }
    })
}
</script>

<style scoped>
.login-container {
  width: 40%; /* 너비를 전체의 40%로 설정 */
  margin: 100px auto;
  padding: 20px;
  background-color: #f0f8ff;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

h1 {
  color: #1e90ff;
  margin-bottom: 20px;
  font-size: 2em;
  font-weight: bold;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 20px;
  text-align: left;
}

label {
  font-weight: bold;
  color: #1e90ff;
  margin-bottom: 5px;
  display: block;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 12px;
  margin-top: 5px;
  border: 2px solid #87cefa;
  border-radius: 5px;
  font-size: 1em;
  transition: border-color 0.3s ease-in-out;
}

input[type="text"]:focus,
input[type="password"]:focus {
  outline: none;
  border-color: #1e90ff;
  box-shadow: 0 0 5px rgba(30, 144, 255, 0.5);
}

.login-button {
  background-color: #1e90ff;
  color: white;
  border: none;
  padding: 15px;
  border-radius: 25px;
  font-size: 1.2em;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 20px;
}

.login-button:hover {
  background-color: #4682b4;
  transform: translateY(-3px);
  box-shadow: 0 8px 15px rgba(30, 144, 255, 0.4);
}

.login-button:active {
  transform: translateY(0);
  box-shadow: 0 4px 10px rgba(30, 144, 255, 0.2);
}

body {
  font-family: 'Inter', sans-serif;
  background-color: #e6f7ff;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
