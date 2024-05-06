# backend/consumers.py

import json
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
import time
import requests

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        print('有人来连接了')
        self.accept()

    def websocket_receive(self, message):
        print("接收到消息--》",message["text"])
        aa = message['text']
        print(aa)
        self.send('====================开始处理自动接单程序===================')
        self.send(f'你输入的订单为：{aa}')
        time.sleep(1)
        self.send('任务进程 ｜ 接单成功')
        time.sleep(1)
        self.send('任务进程 ｜ 开始裁床排单')
        time.sleep(1)
        self.send('任务进程 ｜ 开始录入裁数')
        time.sleep(1)
        self.send('任务进程 ｜ 开始车缝排单')
        time.sleep(1)
        self.send('任务进程 ｜ 开始车缝中')
        time.sleep(1)
        self.send('任务进程 ｜ 车缝已完成')
        time.sleep(1)
        self.send('任务进程 ｜ 开始后整排单')
        time.sleep(1)
        self.send('任务进程 ｜ 开始后整中')
        time.sleep(1)
        self.send('任务进程 ｜ 后整已完成，可进入发货阶段')




    def websocket_disconnect(self, message):
        print('断开连接')
        raise StopConsumer()

class OrderConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        print('有人来连接了,hahahah')
        self.accept()

    def websocket_receive(self, message):
        print("接收到消息--》",message)
        aa = message['text']

        self.send(f'====================开始处理{aa}订单===================')
        self.send(f'你下的购物车商品单号为：{aa}')
        time.sleep(1)
        self.send('任务进程 ｜ 已加入购物车')
        time.sleep(1)
        self.send('任务进程 ｜ 初审通过')
        time.sleep(1)
        self.send('任务进程 ｜ 复审通过')
        time.sleep(1)
        self.send(f'任务进程 ｜ 付款成功，预计3天后收获，商品编号为：{aa}\n\n')


    def websocket_disconnect(self, message):
        print('断开连接')
        raise StopConsumer()

