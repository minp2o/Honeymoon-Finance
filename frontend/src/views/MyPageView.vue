<template>
  <div class="my-page-container">
    <h1>마이페이지</h1>
    <div v-if="isLogin">
      <p><strong>이름:</strong> {{ user.username }}</p>
      <p><strong>닉네임:</strong> {{ user.nickname }}</p>
      <p><strong>이메일:</strong> {{ user.email }}</p>
      <p><strong>전화번호:</strong> {{ user.phone }}</p>

      
      <!-- 사용자에게 추가 정보를 보여주려면 다음과 같이 확장할 수 있습니다. -->
      <p v-if="user.age"><strong>나이:</strong> {{ user.age }}</p>
      <p v-if="user.gender"><strong>성별:</strong> {{ user.gender }}</p>

    </div>
    <div v-else class="login-prompt">
      <p>로그인이 필요합니다. 로그인 페이지로 이동합니다.</p>
      <RouterLink :to="{ name: 'LogInView' }" class="login-link">로그인</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const router = useRouter()

// 로그인 상태 확인
const isLogin = computed(() => store.isLogin)

// 사용자 정보 저장
const user = ref({})

// 사용자 정보를 가져오는 함수
const fetchUserProfile = function () {
  if (isLogin.value) {
    console.log('Fetching user profile...') // 콘솔 로그로 확인
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/dj-rest-auth/user/',
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) => {
        console.log('User profile response:', res.data) // 응답 데이터 확인
        user.value = res.data
      })
      .catch((err) => {
        console.error('프로필 정보 가져오기 실패:', err)
        if (err.response && err.response.status === 401) {
          alert('로그인 세션이 만료되었습니다. 다시 로그인해주세요.')
          store.token = null
          router.push({ name: 'LogInView' })
        }
      })
  } else {
    router.push({ name: 'LogInView' })
  }
}




// 컴포넌트가 마운트될 때 사용자 정보 가져오기
onMounted(() => {
  fetchUserProfile()
})
</script>

<style scoped>
.my-page-container {
  width: 40%;
  margin: 50px auto;
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

.logout-button {
  background-color: #1e90ff;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 25px;
  font-size: 1em;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 20px;
}

.logout-button:hover {
  background-color: #4682b4;
  transform: translateY(-3px);
  box-shadow: 0 8px 15px rgba(30, 144, 255, 0.4);
}

.logout-button:active {
  transform: translateY(0);
  box-shadow: 0 4px 10px rgba(30, 144, 255, 0.2);
}

.login-prompt {
  font-size: 1.2em;
  color: #2c3e50;
}

.login-link {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #1e90ff;
  color: white;
  text-decoration: none;
  border-radius: 25px;
  transition: background-color 0.3s ease;
}

.login-link:hover {
  background-color: #4682b4;
}
</style>

