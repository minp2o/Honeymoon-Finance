<template>

    <div class="chat-container">
        <h1 id="title">무엇이든 물어보세요!</h1>
      <div class="chat-messages">
        <div v-for="(message, index) in messages" :key="index" :class="message.role">
          {{ message.content }}
        </div>
      </div>
      <div class="chat-input">
        <input v-model="userInput" @keyup.enter="sendMessage" placeholder="메시지를 입력하세요...">
        <button @click="sendMessage">전송</button>

      </div>
    </div>
  </template>

  <script>
  import axios from 'axios';
  const apiKey = import.meta.env.VITE_OPENAI_API_KEY;
  
  export default {
    data() {
      return {
        messages: [],
        userInput: '',
      };
    },
    methods: {
      async sendMessage() {
        if (!this.userInput.trim()) return;
  
        const userMessage = { role: 'user', content: this.userInput };
        this.messages.push(userMessage);
        this.userInput = '';
  
        try {
          const response = await axios.post('https://api.openai.com/v1/chat/completions', {
            model: 'gpt-3.5-turbo',
            messages: [
              { role: 'system', content: 'You are a helpful assistant.' },
              ...this.messages
            ]
          }, {
            headers: {

              'Authorization': `Bearer ${apiKey}`,
              'Content-Type': 'application/json'
            }
          });
  
          const assistantMessage = response.data.choices[0].message;
          this.messages.push(assistantMessage);
        } catch (error) {
          console.error('Error:', error);
          this.messages.push({ role: 'assistant', content: '죄송합니다. 오류가 발생했습니다.' });
        }
      }
    }
  };
  </script>

  <style scoped>

#title{
    color: #2196f3;
    text-align: center;
    font-size: 24px;
    margin-bottom: 20px;
    font-weight: 600;
    letter-spacing: 0.5px;
}

.chat-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.chat-messages {
  height: 400px;
  overflow-y: auto;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 10px;
  margin-bottom: 20px;
}

.chat-messages div {
  margin-bottom: 10px;
  padding: 8px 12px;
  border-radius: 18px;
  max-width: 70%;
}

.chat-messages .user {
  background-color: #e3f2fd;
  align-self: flex-end;
  margin-left: auto;
}

.chat-messages .assistant {
  background-color: #f5f5f5;
  align-self: flex-start;
}

.chat-input {
  display: flex;
  gap: 10px;
}

input {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  font-size: 16px;
}

button {
  padding: 10px 10px;
  background-color: #2196f3;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #1976d2;
}
</style>
  

