import { createRouter, createWebHistory } from 'vue-router'

import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import MyPageView from '@/views/MyPageView.vue'
import LoanView from '@/views/LoanView.vue'
import Compare from '@/components/Compare.vue'
import FinancialSurvey from '@/views/FinancialSurvey.vue'
import { useCounterStore } from '@/stores/counter'
import HomeView from '../views/HomeView.vue'
import MainPage from '../components/MainPage.vue'
import CurrencyConverter from '../views/CurrencyConverter.vue'
import ExchangeRates from '../views/ExchangeRates.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },

    {
      path: '/survey',
      name: 'FinancialSurvey',
      component: FinancialSurvey
    },

    {
      path: '/loan',
      name: 'LoanView',
      component: LoanView
    },

    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/myPage',
      name: 'MyPageView',
      component: MyPageView
    },

    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/CurrencyConverter',
      name: 'CurrencyConverter',
      component: CurrencyConverter
    },
    {
      path: '/exchange-rates',
      name: 'ExchangeRates',
      component: ExchangeRates
    },
    {
      path: '/compare',
      name: 'Compare',
      component: Compare,
    },
  ]
})



export default router