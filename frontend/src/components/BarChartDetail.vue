<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/users'
// Vuetify 3.x에서 색상 유틸리티를 가져오기
import { useTheme } from 'vuetify'  // Vuetify 3.x에서 색상을 가져오는 올바른 방법
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

// Vuetify 테마에서 색상 유틸리티 가져오기
const theme = useTheme()

const userStore = useUserStore()

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const props = defineProps({
  title: String,
  averageIntrRate: Array,
  intrRate: Array,
  intrRate2: Array
})

// 차트 데이터 설정
const chartData = {
  labels: ['6개월 금리', '12개월 금리', '24개월 금리', '36개월 금리'],
  datasets: [
    {
      label: '평균 금리',
      data: props.averageIntrRate,
      backgroundColor: theme.themeRef.value.colors.grey.base, // Vuetify 색상 가져오기
      stack: 'Stack 0'
    },
    {
      label: '저축 금리',
      data: props.intrRate2,
      backgroundColor: '#1089FF', // 하드코딩된 색상
      stack: 'Stack 1'
    },
    {
      label: '최고 우대 금리',
      data: props.intrRate2,
      backgroundColor: theme.themeRef.value.colors.red.accent2, // Vuetify 색상 가져오기
      stack: 'Stack 2'
    },
  ]
}

// 차트 옵션 설정
const chartOptions = ref({
  plugins: {
    title: {
      display: true,
      text: `<${props.title}> 상품의 저축 금리`
    },
  },
  responsive: true,
  scales: {
    x: {
      stacked: true,
      ticks: {
        maxRotation: 0,
        minRotation: 0,
        font: {
          size: 10
        }
      }
    },
  },
})
</script>

<template>
  <div>
    <Bar
      class="mx-auto"
      style="width: 100%;"
      :options="chartOptions"
      :data="chartData"
    />
  </div>
</template>

<style scoped>

</style>