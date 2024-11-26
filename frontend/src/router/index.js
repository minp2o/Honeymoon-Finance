import { createRouter, createWebHistory } from 'vue-router'

import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import MyPageView from '@/views/MyPageView.vue'
import LoanView from '@/views/LoanView.vue'
import Compare from '@/components/Compare.vue'
import CompareListView from '@/views/CompareListView.vue'
import DepositList from '@/components/DepositList.vue'
import SavingList from '@/components/SavingList.vue'
import MapView from '@/views/MapView.vue'
import { useCounterStore } from '@/stores/counter'
import HomeView from '../views/HomeView.vue'
import MainPage from '../components/MainPage.vue'
import CurrencyConverter from '../views/CurrencyConverter.vue'
import ExchangeRates from '../views/ExchangeRates.vue'
import NotFound from '@/components/NotFound.vue'
import PostListView from '../views/PostListView.vue'
import ChatBot from '@/components/ChatBot.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },

    {
      path: '/chatbot',
      name: 'ChatBot',
      component: ChatBot
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
      component: CompareListView,
      children: [
        {
          path: 'deposit',
          name: 'depositList',
          component: DepositList,
        },
        {
          path: 'saving',
          name: 'savingList',
          component: SavingList,
        },
      ]
    },
    {
      path: '/bank',
      name: 'bankMap',
      component: MapView
    },
    {
      path: '/404',
      name: 'notFound',
      component: NotFound
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: "/404"
    },
    {
      path: '/map',
      name: 'MapView',
      component: MapView
    },
    {
      path: '/posts',
      name: 'PostListView',
      component: PostListView
    },
  ]
})



export default router

// import { createRouter, createWebHistory } from 'vue-router';

// import HomeView from '@/views/HomeView.vue';
// import NotFound from '@/components/NotFound.vue';
// import CompareListView from '@/views/CompareListView.vue';
// import DepositList from '@/components/DepositList.vue';
// import SavingList from '@/components/SavingList.vue';
// import ExchangeView from '@/views/ExchangeView.vue';
// import MapView from '@/views/MapView.vue';
// import PostListView from '@/views/PostListView.vue';
// import PostDetailView from '@/views/PostDetailView.vue';
// import PostCreateView from '@/views/PostCreateView.vue';
// import PostUpdateView from '@/views/PostUpdateView.vue';
// import SignUpView from '@/views/SignUpView.vue';
// import SignInView from '@/views/SignInView.vue';
// import MyPageView from '@/views/MyPageView.vue';
// import MyPage from '@/components/MyPage.vue';
// import ProductManage from '@/components/ProductManage.vue';
// import ProductRecommend from '@/components/ProductRecommend.vue';
// import CreateView from '@/views/CreateView.vue';
// import CurrencyConverter from '@/views/CurrencyConverter.vue';
// import ExchangeRates from '@/views/ExchangeRates.vue';
// import Compare from '@/components/Compare.vue';

// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   routes: [
//     {
//       path: '/',
//       name: 'home',
//       component: HomeView,
//     },
//     {
//       path: '/create',
//       name: 'CreateView',
//       component: CreateView,
//     },
//     {
//       path: '/signup',
//       name: 'SignUpView',
//       component: SignUpView,
//     },
//     {
//       path: '/signin',
//       name: 'SignInView',
//       component: SignInView,
//     },
//     {
//       path: '/mypage/:username*',
//       component: MyPageView,
//       children: [
//         {
//           path: '',
//           name: 'myPage',
//           component: MyPage,
//         },
//         {
//           path: 'products',
//           name: 'productManage',
//           component: ProductManage,
//         },
//         {
//           path: 'recommend',
//           name: 'productRecommend',
//           component: ProductRecommend,
//         },
//       ],
//     },
//     {
//       path: '/compare',
//       component: CompareListView,
//       children: [
//         {
//           path: 'deposit',
//           name: 'depositList',
//           component: DepositList,
//         },
//         {
//           path: 'saving',
//           name: 'savingList',
//           component: SavingList,
//         },
//       ],
//     },
//     {
//       path: '/compare-simple',
//       name: 'Compare',
//       component: Compare,
//     },
//     {
//       path: '/bank',
//       name: 'bankMap',
//       component: MapView,
//     },
//     {
//       path: '/posts',
//       name: 'postList',
//       component: PostListView,
//     },
//     {
//       path: '/posts/:id',
//       name: 'postDetail',
//       component: PostDetailView,
//     },
//     {
//       path: '/posts/write',
//       name: 'postCreate',
//       component: PostCreateView,
//     },
//     {
//       path: '/posts/:id/update',
//       name: 'postUpdate',
//       component: PostUpdateView,
//     },
//     {
//       path: '/CurrencyConverter',
//       name: 'CurrencyConverter',
//       component: CurrencyConverter,
//     },
//     {
//       path: '/exchange-rates',
//       name: 'ExchangeRates',
//       component: ExchangeRates,
//     },
//     {
//       path: '/404',
//       name: 'notFound',
//       component: NotFound,
//     },
//     {
//       path: '/:pathMatch(.*)*',
//       redirect: '/404',
//     },
//   ],
// });

// export default router;
