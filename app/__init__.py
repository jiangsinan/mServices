import os

from tornado.web import Application

from app.views.cookie_v import CookieHandler
from app.views.index_v import IndexHandler
from app.views.order_v import OrderHandler
from app.views.search_v import SearchHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = {
    'debug':True,
    'template_path':os.path.join(BASE_DIR,'templates')
}

def make_app(host='localhost'):
    return Application(handlers =[
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        (r'/order/(?P<action_code>\d+)/(?P<order_id>\d+)',OrderHandler),
    ],
        default_host=host,**settings)