
<template>
  <header>
    <nav>
      <RouterLink to="/">홈</RouterLink> |
      <RouterLink to="/compare/deposit">상품조회</RouterLink>
      <RouterLink to="/loan">전세자금대출조회</RouterLink>
      <RouterLink to="/posts">게시판</RouterLink>
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
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { computed } from 'vue'
import { RouterView, RouterLink, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const router = useRouter()

// 로그인 상태 확인 (반응성 유지)
const isLogin = computed(() => store.isLogin)

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
  padding: 30px;
  text-align: center;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  margin: 0 10px;
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
</style>
