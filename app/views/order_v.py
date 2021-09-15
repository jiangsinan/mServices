from tornado.web import RequestHandler
class OrderHandler(RequestHandler):
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