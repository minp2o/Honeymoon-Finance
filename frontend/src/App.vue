
<template>
  <header>
    <nav>
      <RouterLink to="/">홈</RouterLink> |
      <RouterLink to="/compare/deposit">상품조회</RouterLink>
      <RouterLink to="/loan">전세자금대출조회</RouterLink>
      <RouterLink to="/exchange-rates">환율 조회</RouterLink>
      <RouterLink to="/map">주변은행</RouterLink>
      
      <!-- 로그인되지 않은 상태에서 회원가입/로그인 버튼 표시 -->
      <span v-if="!isLogin">
        | <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
        <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink>
      </span>

      <!-- 로그인된 상태에서 마이페이지, 로그아웃 버튼 표시 -->
      <span v-if="isLogin">
        <RouterLink :to="{ name: 'MyPageView' }">마이페이지</RouterLink> 
        <button @click.prevent="logOut" class="logout-button">로그아웃</button>
      </span>
      <button @click="toggleChatbot" class="help-button">도움</button>
      
    </nav>
  </header>
  <RouterView />
  <!-- 챗봇 컴포넌트 -->
  <Transition name="slide">
    <div v-if="showChatbot" class="chatbot-sidebar">
      <button @click="toggleChatbot" class="close-button">&times;</button>
      <ChatBot />
    </div>
  </Transition>
</template>

<script setup>
import ChatBot from './components/ChatBot.vue'

import { computed, ref } from 'vue'
import { RouterView, RouterLink, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const router = useRouter()

// 로그인 상태 확인 (반응성 유지)
const isLogin = computed(() => store.isLogin)


// 챗봇 표시 여부를 관리하는 상태
const showChatbot = ref(false)

// 챗봇 토글 함수
const toggleChatbot = () => {
  showChatbot.value = !showChatbot.value
}

// 로그아웃 함수 정의
const logOut = function () {
  store.logOut()
    .then(() => {
      router.push({ name: 'HomeView' }) // 로그아웃 후 홈 화면으로 리다이렉트
    })
    .catch((err) => {
      console.error('로그아웃 실패:', err)
    })
}
</script>

<style scoped>
#app {
  font-family: 'Inter', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

nav {
  padding-top: 30px;
  text-align: center;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  margin: 0 15px;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.logout-button {
  background-color: transparent;
  border: none;
  color: #2c3e50;
  font-weight: bold;
  cursor: pointer;
  text-decoration: underline;
  margin-left: 10px;
}

.logout-button:hover {
  color: #42b983;
}
.help-button {
  position: fixed;
  right: 30px;
  top: 30px;
  background-color: #42b983;
  color: white;
  padding: 8px 15px;
  border-radius: 20px;
  border: none;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.help-button:hover {
  background-color: #3aa876;
}

.chatbot-sidebar {
  position: fixed;
  top: 0;
  right: 0;
  width: 300px;
  height: 100vh;
  background-color: white;
  box-shadow: -2px 0 5px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  padding: 20px;
  overflow-y: auto;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

/* 슬라이드 애니메이션 */
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
  transform: translateX(100%);
}
</style>
