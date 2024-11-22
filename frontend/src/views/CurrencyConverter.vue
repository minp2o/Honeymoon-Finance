<template>
    <div>
      <h1>환율 조회</h1>
      <select v-model="baseCurrency">
        <option v-for="(rate, code) in exchangeRates" :key="code" :value="code">
          {{ code }}
        </option>
      </select>
      <ul>
        <li v-for="(rate, code) in exchangeRates" :key="code">
          {{ code }}: {{ (rate / exchangeRates[baseCurrency]).toFixed(4) }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        baseCurrency: 'USD',
        exchangeRates: {},
      };
    },
    mounted() {
      this.fetchExchangeRates();
    },
    methods: {
      async fetchExchangeRates() {
        try {
          const apiKey = process.env.VUE_APP_EXCHANGE_API_KEY;
          const response = await axios.get(`https://v6.exchangerate-api.com/v6/${apiKey}/latest/USD`);
          this.exchangeRates = response.data.conversion_rates;
        } catch (error) {
          console.error('Failed to fetch exchange rates:', error);
        }
      },
    },
    watch: {
      baseCurrency() {
        this.fetchExchangeRates();
      }
    }
  };
  </script>