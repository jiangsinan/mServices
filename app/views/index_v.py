from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def get(self):
        self.render('index.html',msg='Hi，jsn')

    def post(self):
        # wd = self.get_query_argument('wd')
        self.write('<h3>我是主页</h3>')

    def gut(self):
        name = self.get_body_argument('name')
        city = self.get_body_argument('city')
        self.write('<h3>%s %s</h3>' % (name, city))

