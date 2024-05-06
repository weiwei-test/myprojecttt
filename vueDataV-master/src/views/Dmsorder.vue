<template>
    <div>
      <div class="container">
        <div class="son-container">
          <div class="input-group">
            <label for="sku" class="skuu">商品id：</label>
            <input type="text" id="sku" v-model="sku" @keyup.enter="fetchSize" class="input-field">
          </div>
          <div class="input-group">
            <label for="stock-type">商品类型：</label>
            <select id="stock-type" v-model="stockType" class="select-field">
              <option value="normal">普通商品</option>
              <option value="jit">贵重商品</option>
            </select>
          </div>
          <div class="input-group">
            <label for="order-quantity">订单数量：</label>
            <input type="number" id="order-quantity" v-model="orderQuantity" class="select-field">
          </div>
          <div class="input-group">
            <label class="size-label">商品条码：</label>
            <div v-for="(size, index) in sizes" :key="index">
              <input type="text" v-model="quantity[index]" :placeholder="sizes[index]['sku']" class="size-input">
            </div>
          </div>
          <div>
            <button @click="orderbutton" class="order-button">一键下单</button>
          </div>
        </div>
        <div class="log">
          <h3 class="logview" align="center">下单跟进日志</h3>
          <textarea v-model="receivedMessagess" rows="10" cols="50" readonly class="message-box"></textarea>
          <h3 class="logview" align="center">返回参数</h3>
          <textarea v-model="receivedMessages" rows="10" cols="50" readonly class="message-box"></textarea>
        </div>
      </div>
    </div>
  
  </template>
  
  <script>
  export default {
    data() {
      return {
        sku: '',
        stockType: 'normal',
        orderQuantity: '',
        quantity: [],
        sizes: [], // 存储尺码的数组
        receivedMessages: '',
        receivedMessagess: []
      };
    },
  
    mounted() {
      this.connectWebSocket()
    },
  
    methods: {
  
      connectWebSocket() {
        // Replace 'ws://localhost:8000/ws/' with your WebSocket server URL
        this.socket = new WebSocket('ws://localhost:8000/order/chat/');
  
        this.socket.onmessage = event => {
          this.receivedMessagess += event.data + '\n';
        };
        this.socket.onclose = () => {
          console.log('WebSocket closed. Reconnecting...');
          this.connectWebSocket();
        };
      },
  
      async orderbutton() {
        this.receivedMessages = '';
        this.receivedMessagess='';
        const datatosend = this.sizes.map((size, index) => ({
          size: size,
          quantity: this.quantity[index]
        }));
  
        // 调用后端API获取尺码信息
        const times = parseInt(this.orderQuantity);
        for (let i = 0; i < times; i++) {
          try {
            let stockTypeEnumValue = '';
            let combinedData = [];
            if (this.stockType === 'normal') {
              stockTypeEnumValue = 'NORMAL';
            } else if (this.stockType === 'jit') {
              stockTypeEnumValue = 'JIT';
            }
            const response = await this.$API.order.order({
              'orderQuantity': this.orderQuantity,
              'stockType': stockTypeEnumValue,
              'skc': this.sku,
              'skulist': datatosend
            });
            console.log(response.info)
            if (response.code === 20000) {
              this.receivedMessages += ('第' + (i + 1) + '个订单为：' + JSON.stringify(response.info)) + '\n\n'
              combinedData=response.info[0]['dmsid'];
              this.socket.send(combinedData)
            } else {
              console.error('Error:', 'sdsf');
            }
          } catch (error) {
            console.error('Error', error);
          }
        }
  
  
      },
  
      async fetchSize() {
        if (this.sku.trim() === '') return; // 如果SKU输入为空，则不调用后端API
        try {
          const response = await this.$API.order.size({'skc': this.sku});
          if (response.code === 20000) {
            this.sizes = response.info;
          } else {
            console.error('Error', 'shujucuowu');
          }
        } catch (error) {
          console.error('Error', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: row;
    margin-left: 3%;
  }
  
  .input-group {
    margin-bottom: 20px;
  }
  
  .input-field {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 100%;
    margin-left: 30px;
  }
  
  .skuu {
    margin-left: 30px;
  }
  
  .size-label {
    margin-left: 30px;
  }
  
  .select-field {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 100%;
    box-sizing: border-box;
    margin-top: 5px;
    margin-left: 30px;
  
  }
  
  .size-input {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 100%;
    box-sizing: border-box;
    margin-top: 5px;
    margin-left: 30px;
  }
  
  .log {
    margin-left: 30%;
    margin-top: 0px;
  }
  
  .order-button {
    padding: 10px 20px;
    border: none;
    border-radius: 10px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
    margin-left: 155px;
  }
  
  .size-input {
    width: calc(100% - 5px); /* 尺码输入框宽度根据列数自动调整 */
    margin-right: 5px;
  }
  
  .message-box {
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 10px;
    width: 600px;
    height: 300px;
    margin-bottom: 10px;
  }
  </style>
  