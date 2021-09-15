import json

import tornado.web
from tornado.ioloop import IOLoop
import tornado.options


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # wd = self.get_query_argument('wd')
        self.write('<h3>我是主页</h3>')

    def post(self):
        name = self.get_body_argument('name')
        city = self.get_body_argument('city')
        self.write('<h3>%s %s</h3>' % (name, city))

    def delete(self):
        print('delete')
        self.write('<h3>我是delete</h3>')

    def put(self):
        print('put')
        self.write('<h3>我是put</h3>')


class SearchHandler(tornado.web.RequestHandler):
    mapper = {
        'python': 'Python是目前世界最流行的AI语言',
        'java': 'Java已经是20多年企业家应用开发语言',
        'H5': 'H5是'
    }

    def get(self):
        html = """
        <h3>搜索%s结果</h3>
        <p>
            %s
        </p>
        """
        wd = self.get_query_argument('wd')
        result = self.mapper.get(wd)
        resp_data = {
            'wd': wd,
            'result': result
        }

        self.write(json.dumps(resp_data))
        self.set_status(200)
        self.set_header('Content-Type', 'application/json;charset = utf-8')
        self.set_cookie('wd', wd)


class CookieHandler(tornado.web.RequestHandler):
    def get(self):
        if self.request.arguments.get('name'):
            name = self.get_query_argument('name')
            value = self.get_cookie(name)
            self.write(value)
        else:
            cookies: dict = self.request.cookies
            html = '<ul>%s</ul>'
            list = []
            for key in cookies:
                list.append('<li>%s:%s</li>' % (key, self.get_cookie(key)))
            self.write('显示所有Cookie' + html % ''.join(list))

    def delete(self):
        name = self.get_query_argument('name')
        if self.request.cookies.get(name, None):
            self.clear_cookie(name)
            self.write('删除%s成功' % name)
        else:
            self.write('删除%s失败' % name)

class OrderHandler(tornado.web.RequestHandler):
    goods = [
        {
            'id':1,
            'name':'Pyhon',
            'author':'jsn',
            'price':190
        },
        {
            'id': 2,
            'name': 'Java',
            'author': 'yky',
            'price': 250
        },
    ]
    action_map = {
        1:'取消订单',
        2:'再次购买',
        3:'评价'
    }
    def query(self,order_id):
        for item in self.goods:
            if item.get('id') == order_id:
                return item
    def get(self,order_id,action_code):
        html = """
            <h3>订单查询</h3>
            <p>
                商品编号:%s
            </p>
            <p>
                商品名称:%s
            </p>
            <p>
                商品价格:%s
            </p>
        """
        goods = self.query(int(order_id))
        self.write(html%(goods.get('id'),goods.get('name'),goods.get('price')))
        self.write(self.action_map.get(int(action_code)))

def make_app():
    return tornado.web.Application([
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<action_code>\d+)/(?P<order_id>\d+)',OrderHandler),
    ], default_host=tornado.options.options.host)


if __name__ == '__main__':
    tornado.options.define('port', default=8000, type=int, help='bind socket port')
    tornado.options.define('host', default='localhost', type=str, help='设置host name')
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(tornado.options.options.port)
    print('starting Web Server http://%s:%s' % (tornado.options.options.host, tornado.options.options.port))
    IOLoop.current().start()
