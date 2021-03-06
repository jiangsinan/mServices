from tornado.web import UIModule
from utils.conn import session
from app.models.menu_m import Menu
class MenuModule(UIModule):
    def render(self, *args, **kwargs):
        data = {
            'menus':session.query(Menu).filter(Menu.parent_id.is_(None)).all()
        }
        return self.render_string('ui/menu.html',**data)