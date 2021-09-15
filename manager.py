import json
from tornado.ioloop import IOLoop
import tornado.options as options
from app import make_app

if __name__ == '__main__':
    options.define('port', default=8000, type=int, help='bind socket port')

    options.define('host', default='localhost', type=str, help='设置host name')

    options.parse_command_line()

    app = make_app(options.options.port)

    app.listen(options.options.port)

    print('starting Web Server http://%s:%s' % (options.options.host, options.options.port))

    IOLoop.current().start()
