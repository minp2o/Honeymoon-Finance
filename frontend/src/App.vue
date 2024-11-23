<template>
  <header>
    <nav>
      <RouterLink to="/">홈</RouterLink> |
      <RouterLink to="/compare">상품조회</RouterLink>
      <RouterLink to="/posts">게시판</RouterLink>
      <Router-link to="/exchange-rates">환율 조회</router-link>
      <RouterLink to="/posts">주변은행</RouterLink>
      <RouterLink to="/posts">금융교육</RouterLink>
      <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink> |
      <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink> | 
      <form @submit.prevent="logOut">
        <input type="submit" value="Logout">
      </form>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>

import { RouterView, RouterLink,useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'


const store = useCounterStore()

const logOut = function () {
  store.logOut()
}
</script>


<style>
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
</style>