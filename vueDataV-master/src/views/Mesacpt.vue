<template>
  <div class="container">
    <div class="input-containerr">
      <div class="input-container">
        <h3 class="fontview" align="center">请输入待接单订单号</h3>
        <input type="text" v-model="messagee" placeholder="输入待接单订单" class="input-field">
        <div class="button-container">
          <button @click="sendMessage" class="send-button">一键接单</button>
          <button @click="clearMessages" class="clear-button">清空内容</button>
        </div>
      </div>
      <div>
        <h4 class="logview" align="center">订单接单状态跟进日志</h4>
        <textarea v-model="receivedMessages" rows="10" cols="50" readonly class="message-box"></textarea>
      </div>
    </div>
    <hr class="line">
    <div>
      <h2>生活不可能像你想象得那么好，但也不会像你想象得那么糟    ---莫泊桑</h2>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messagee: '',
      receivedMessages: '',
      hahaha: 'lalalalal'
    }
  },
  mounted() {
    this.connectWebSocket();
  },
  methods: {
    connectWebSocket() {
      // Replace 'ws://localhost:8000/ws/' with your WebSocket server URL
      this.socket = new WebSocket('ws://localhost:8000/ws/chat/');

      this.socket.onmessage = event => {
        this.receivedMessages += event.data + '\n';
      };
      this.socket.onclose = () => {
        console.log('WebSocket closed. Reconnecting...');
        this.connectWebSocket();
      };
    },
    sendMessage() {
      const datalist = JSON.stringify({
        'name1': this.messagee,
        'name2': this.hahaha
      });

      if (this.messagee.trim() !== '') {
        this.socket.send(datalist);
        this.message = '';
      }
    },
    clearMessages() {
      this.receivedMessages = '';
    }
  }
}
</script>

<style scoped>
.input-containerr {
  display: flex;
  flex-direction: row;
}

.fontview {
  margin-top: 200px;
  margin-bottom: 1px;
}

.logview {
  margin-left: 100px;
  margin-bottom: 1px;
}

.input-container {
  margin-bottom: 10px;
  margin-left: 15%
}

.input-field {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin-right: 10px;
  width: 300px;
  margin-bottom: 10px;
}

.send-button {
  padding: 10px 20px;
  border: none;
  border-radius: 50px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
  margin-left: 15px;
}

.clear-button {
  padding: 10px 20px;
  border: none;
  border-radius: 50px;
  background-color: #236446;
  color: white;
  cursor: pointer;
  margin-left: 60px;
}

.line {
  width: 100%;
  border: none;
  border-top: 2px solid #3f9428;
  margin-top: 100px;
  margin-bottom: 20px;
}

.message-box {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  width: 600px;
  height: 400px;
  margin-left: 100px;
}
h2{
  text-align: center;
  font-size: 20px;
}

</style>