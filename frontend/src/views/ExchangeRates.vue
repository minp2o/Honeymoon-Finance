<!-- <template>
    <div>
      <h1>환율 조회</h1>
      <p>이 페이지는 환율조회 페이지입니다.</p>
      <form @submit.prevent="convertCurrency">
        <label for="amount">Amount:</label>
        <input v-model="amount" type="number" id="amount" required />
  
        <label for="fromCurrency">From Currency:</label>
        <select v-model="fromCurrency" id="fromCurrency" required>
          <option v-for="(rate, code) in exchangeRates" :key="code" :value="code">
            {{ code }}
          </option>
        </select>
  
        <label for="toCurrency">To Currency:</label>
        <select v-model="toCurrency" id="toCurrency" required>
          <option v-for="(rate, code) in exchangeRates" :key="code" :value="code">
            {{ code }}
          </option>
        </select>
  
        <button type="submit">Convert</button>
      </form>
  
      <div v-if="convertedAmount !== null">
        <h2>Converted Amount: {{ convertedAmount }}</h2>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        amount: 0,
        fromCurrency: 'USD',
        toCurrency: 'EUR',
        exchangeRates: {},
        convertedAmount: null,
      };
    },
    mounted() {
      this.fetchExchangeRates();
    },
    methods: {
      async fetchExchangeRates() {
        try {
          // Vue에서 환경 변수 사용
          const apiKey = process.env.VUE_APP_EXCHANGE_API_KEY;
          const response = await axios.get(`https://v6.exchangerate-api.com/v6/${apiKey}/latest/USD`);
          this.exchangeRates = response.data.conversion_rates;
        } catch (error) {
          console.error('Failed to fetch exchange rates:', error);
        }
      },
      convertCurrency() {
        if (this.exchangeRates[this.fromCurrency] && this.exchangeRates[this.toCurrency]) {
          const fromRate = this.exchangeRates[this.fromCurrency];
          const toRate = this.exchangeRates[this.toCurrency];
          this.convertedAmount = (this.amount * (toRate / fromRate)).toFixed(2);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* 스타일링 */
  </style>
   -->
<!-- ------------------------ -->
<!-- vue
<template>
  <div class="currency-converter">
    <h1>환율 조회</h1>
    <p>이 페이지는 환율조회 페이지입니다. 원하는 금액과 통화를 선택하여 변환하세요!</p>
    
    <form @submit.prevent="convertCurrency" class="converter-form">
      <div class="form-group">
        <label for="amount">Amount:</label>
        <input
          v-model="amount"
          type="number"
          id="amount"
          placeholder="Enter amount"
          required
          class="input-field"
        />
      </div>

      <div class="form-group">
        <label for="fromCurrency">From Currency:</label>
        <select v-model="fromCurrency" id="fromCurrency" required class="select-field">
          <option v-for="(rate, code) in exchangeRates" :key="code" :value="code">
            {{ code }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="toCurrency">To Currency:</label>
        <select v-model="toCurrency" id="toCurrency" required class="select-field">
          <option v-for="(rate, code) in exchangeRates" :key="code" :value="code">
            {{ code }}
          </option>
        </select>
      </div>

      <button type="submit" class="convert-button">Convert</button>
    </form>

    <div v-if="loading" class="loading-message">Loading exchange rates...</div>
    <div v-if="error" class="error-message">{{ error }}</div>
    <div v-if="convertedAmount !== null" class="result">
      <h2>Converted Amount: {{ convertedAmount }} {{ toCurrency }}</h2>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      amount: 0,
      fromCurrency: 'USD',
      toCurrency: 'EUR',
      exchangeRates: {},
      convertedAmount: null,
      loading: false,
      error: null,
    };
  },
  mounted() {
    this.fetchExchangeRates();
  },
  methods: {
    async fetchExchangeRates() {
      this.loading = true;
      this.error = null;
      try {
        const apiKey = process.env.VUE_APP_EXCHANGE_API_KEY;
        const response = await axios.get(`https://v6.exchangerate-api.com/v6/${apiKey}/latest/USD`);
        this.exchangeRates = response.data.conversion_rates;
      } catch (error) {
        this.error = 'Failed to fetch exchange rates. Please try again later.';
        console.error('Failed to fetch exchange rates:', error);
      } finally {
        this.loading = false;
      }
    },
    convertCurrency() {
      if (this.exchangeRates[this.fromCurrency] && this.exchangeRates[this.toCurrency]) {
        const fromRate = this.exchangeRates[this.fromCurrency];
        const toRate = this.exchangeRates[this.toCurrency];
        this.convertedAmount = (this.amount * (toRate / fromRate)).toFixed(2);
      }
    },
  },
};
</script>

<style scoped>
.currency-converter {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  color: #333;
}

p {
  text-align: center;
  color: #666;
}

.converter-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.label {
  font-weight: bold;
}

.input-field,
.select-field {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

.convert-button {
  padding: 10px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

.convert-button:hover {
  background-color: #0056b3;
}

.loading-message,
.error-message {
  text-align: center;
  color: #ff0000;
}

.result {
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  margin-top: 20px;
}
</style> -->

vue
<template>
  <div class="currency-converter">
    <h1>환율 조회</h1>
    <p>이 페이지는 환율조회 페이지입니다. 원하는 금액과 통화를 선택하여 변환하세요!</p>
    
    <form @submit.prevent="convertCurrency" class="converter-form">
      <div class="form-group">
        <label for="amount">Amount:</label>
        <input
          v-model="amount"
          type="number"
          id="amount"
          placeholder="Enter amount"
          required
          class="input-field"
        />
      </div>

      <div class="form-group">
        <label for="fromCurrency">From Currency:</label>
        <select v-model="fromCurrency" id="fromCurrency" required class="select-field">
          <option v-for="(rate, code) in exchangeRates" :key="code" :value="code">
            {{ code }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="toCurrency">To Currency:</label>
        <select v-model="toCurrency" id="toCurrency" required class="select-field">
          <option v-for="(rate, code) in exchangeRates" :key="code" :value="code">
            {{ code }}
          </option>
        </select>
      </div>

      <button type="submit" class="convert-button">Convert</button>
    </form>

    <div v-if="loading" class="loading-message">Loading exchange rates...</div>
    <div v-if="error" class="error-message">{{ error }}</div>
    <div v-if="convertedAmount !== null" class="result">
      <h2>Converted Amount: {{ convertedAmount }} {{ toCurrency }}</h2>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      amount: 0,
      fromCurrency: 'USD',
      toCurrency: 'EUR',
      exchangeRates: {},
      convertedAmount: null,
      loading: false,
      error: null,
    };
  },
  mounted() {
    this.fetchExchangeRates();
  },
  methods: {
    async fetchExchangeRates() {
      this.loading = true;
      this.error = null;
      try {
        const apiKey = import.meta.env.VITE_APP_EXCHANGE_API_KEY;
        if (!apiKey) {
                throw new Error('API key is not configured');
            }
        const response = await axios.get(`https://v6.exchangerate-api.com/v6/${apiKey}/latest/USD`);
        this.exchangeRates = response.data.conversion_rates;
      } catch (error) {
        this.error = 'Failed to fetch exchange rates. Please try again later.';
        console.error('Failed to fetch exchange rates:', error);
      } finally {
        this.loading = false;
      }
    },
    convertCurrency() {
      if (this.exchangeRates[this.fromCurrency] && this.exchangeRates[this.toCurrency]) {
        const fromRate = this.exchangeRates[this.fromCurrency];
        const toRate = this.exchangeRates[this.toCurrency];
        this.convertedAmount = (this.amount * (toRate / fromRate)).toFixed(2);
      }
    },
  },
};
</script>

<style scoped>
.currency-converter {
  width: 80%;
  margin: 30px auto;
  padding: 20px;
  background-color: #f0f8ff;
  border-radius: 10px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #1e90ff;
  text-align: center;
  margin-bottom: 30px;
  font-size: 2.2em;
}

p {
  text-align: center;
  color: #4169e1;
  font-size: 1.2em;
  margin: 20px 0;
}

.converter-form {
  background-color: #ffffff;
  border: 1px solid #87cefa;
  border-radius: 8px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 20px;
  transition: transform 0.3s ease;
}

.converter-form:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(30, 144, 255, 0.2);
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  color: #1e90ff;
  font-weight: bold;
}

.input-field,
.select-field {
  padding: 12px;
  border: 1px solid #87cefa;
  border-radius: 4px;
  font-size: 16px;
  background-color: #e6f3ff;
}

.convert-button {
  padding: 12px;
  background-color: #1e90ff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.convert-button:hover {
  background-color: #4169e1;
}

.loading-message,
.error-message {
  text-align: center;
  color: #4169e1;
  font-size: 1.2em;
  margin: 20px 0;
}

.result {
  background-color: #ffffff;
  border: 1px solid #87cefa;
  border-radius: 8px;
  padding: 15px;
  margin-top: 20px;
  text-align: center;
}

.result h2 {
  color: #4169e1;
  font-size: 1.3em;
  margin: 0;
}
</style>
