from tornado.web import UIModule

class MenuModule(UIModule):
    def render(self, *args, **kwargs):
        data = {
            'menus':[
                {'title':'百度','url':'https://www.baidu.com'},
                {'title':'京东','url':'https://www.jd.com'},
                {'title':'阿里','url':'https://www.aliyun.com'}
            ]
        }
        return self.render_string('ui/menu.html',**data)