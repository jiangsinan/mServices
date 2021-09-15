from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
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