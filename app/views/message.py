import random
import time

from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler

class RobbitHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('msg/robbit.html')


class MessageHandler(WebSocketHandler):
    def open(self, *args, **kwargs):
        ip = self.request.remote_ip
        self.write_message('您好,%s'% ip)


        self.write_message('starting')
        for i in range(10):
            time.sleep(1)
            num = random.randint(100,1000)
            self.write_message('%s'%num)

        self.write_message('end')
