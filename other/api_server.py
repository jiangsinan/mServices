import json
import uuid

from tornado.web import RequestHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.options import options,define,parse_command_line

class LoginHandler(RequestHandler):
    users = [
        {'id':1,
        'name':'jsn',
        'pwd':'123456'},
    ]
    def get(self):
        bytes = self.request.body
        print(bytes)
        print(self.request.headers.get('Content-Type'))
        content_type = self.request.headers.get('Content-Type')
        if content_type.startswith('application/json'):
            # self.write('json ok')
            json_str = bytes.decode('utf-8')
            json_data = json.loads(json_str)
            self.write(json_data['name'])
            self.write(json_data['pwd'])
            login_user = None
            resp_data = {}
            for user in self.users:
                if user['name'] == json_data['name']:
                    if user['pwd'] == json_data['pwd']:
                        login_user = user
                        break
            if login_user:
                resp_data['msg'] = 'success'
                resp_data['token'] = uuid.uuid4().hex
            else:
                resp_data['msg'] = '查无此用户'
            print(resp_data)
            self.write(resp_data)
            self.set_header('Content-Type','application/json')

        else:
            self.write('json error')
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass

    def options(self, *args, **kwargs):
        self.set_status(200)

def make_app():
    return Application(
        handlers = [
            ('/login',LoginHandler),
    ],
    default_host=options.h
    )

if __name__ == '__main__':
    define('p',default=8000,type=int)
    define('h',default='localhost',type=str)
    parse_command_line()
    app = make_app()
    app.listen(options.p)
    print('starting Web Server http://%s:%s' % (options.h,options.p))
    IOLoop.current().start()