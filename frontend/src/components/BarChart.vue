<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/users'
import { useTheme } from 'vuetify';  // Vuetify 테마 가져오기
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

// Vuetify 테마에서 색상 유틸리티 가져오기
const theme = useTheme()

// 사용자 스토어 가져오기
const userStore = useUserStore()

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const props = defineProps({
  labels: Array,
  intrRate: Array,
  intrRate2: Array
})

// 차트 데이터 설정
const chartData = {
  labels: props.labels,
  datasets: [
    {
      label: '저축 금리',
      data: props.intrRate,
      backgroundColor: '#1089FF',  // 이 색상은 하드코딩 되어 있습니다.
      stack: 'Stack 0'
    },
    {
      label: '최고 우대 금리',
      data: props.intrRate2,
      backgroundColor: theme.themeRef.value.colors.red.accent2,  // Vuetify 3.x 색상 사용
      stack: 'Stack 1'
    }
  ]
}

// 차트 옵션 설정
const chartOptions = ref({
  plugins: {
    title: {
      display: true,
      text: `${userStore.userInfo.name}님의 가입한 상품 금리`
    },
  },
  responsive: true,
  scales: {
    x: {
      stacked: true,
      ticks: {
        maxRotation: 30,
        minRotation: 0,
        font: {
          size: 8
        }
      }
    },
  },
})
</script>

<template>
  <div>
    <Bar
      :options="chartOptions"
      :data="chartData"
    />
  </div>
</template>

<style scoped>
</style>


<template>
  <div>
    <!-- 아무 내용 없이 기본 구조만을 유지 -->
    <p>BarChartDetail Component</p>
  </div>
</template>

<script>
export default {
  name: 'BarChartDetail',
}
</script>

<style scoped>
/* 스타일을 추가할 경우 여기 */
</style>