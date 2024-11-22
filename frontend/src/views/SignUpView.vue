<template>
  <div class="signup-container">
    <h1>회원가입</h1>
    <form @submit.prevent="signUp" class="signup-form">
      <div class="form-group">
        <label for="username">이름</label>
        <input type="text" id="username" v-model.trim="username" required>
      </div>

      <div class="form-group">
        <label for="nickname">닉네임</label>
        <input type="text" id="nickname" v-model.trim="nickname" required>
      </div>

      <div class="form-group">
        <label for="email">이메일</label>
        <input type="email" id="email" v-model.trim="email" required>
      </div>
      
      <div class="form-group">
        <label for="password1">비밀번호</label>
        <input type="password" id="password1" v-model.trim="password1" required>
      </div>

      <div class="form-group">
        <label for="password2">비밀번호 확인</label>
        <input type="password" id="password2" v-model.trim="password2" required>
      </div>

      <div class="form-group">
        <label for="age">나이</label>
        <input type="number" id="age" v-model.number="age" required min="1">
      </div>

      <div class="form-group">
        <label for="gender">성별</label>
        <select id="gender" v-model="gender" required>
          <option value="">선택하세요</option>
          <option value="male">남성</option>
          <option value="female">여성</option>
        </select>
      </div>

      <div class="form-group">
        <label for="phone">핸드폰 번호</label>
        <input type="tel" id="phone" v-model.trim="phone" placeholder="01011112222">
      </div>

      
      <button type="submit" class="submit-btn">가입하기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref('')
const nickname = ref('')
const email = ref('')
const age = ref(null)
const gender = ref('')
const phone = ref('')
const password1 = ref('')
const password2 = ref('')

const store = useCounterStore()

const signUp = function () {
  const payload = {
    username: username.value,
    nickname: nickname.value,
    email: email.value,
    age: age.value,
    gender: gender.value === 'male' ? 'M' : 'F',
    phone: phone.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}
</script>


<style scoped>
.signup-container {
  width: 40%;
  margin: 50px auto;
  padding: 20px;
  background-color: #f0f8ff;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #1e90ff;
  text-align: center;
  margin-bottom: 20px;
}

.signup-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #4169e1;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #87cefa;
  border-radius: 4px;
  font-size: 16px;
}

input:focus {
  outline: none;
  border-color: #1e90ff;
  box-shadow: 0 0 5px rgba(30, 144, 255, 0.5);
}

.submit-btn {
  background-color: #1e90ff;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  align-self: center;
  margin-top: 10px;
}

.submit-btn:hover {
  background-color: #4169e1;
}

select {
  width: 100%;
  padding: 10px;
  border: 1px solid #87cefa;
  border-radius: 4px;
  font-size: 16px;
  background-color: white;
}

select:focus {
  outline: none;
  border-color: #1e90ff;
  box-shadow: 0 0 5px rgba(30, 144, 255, 0.5);
}

input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type="number"] {
  -moz-appearance: textfield;
}
</style>