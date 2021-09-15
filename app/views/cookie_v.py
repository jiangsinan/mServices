from tornado.web import RequestHandler
class CookieHandler(RequestHandler):
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
