from unittest import TestCase
from utils.conn import session, Base
from app.models.menu_m import Menu


class TestMenuORM(TestCase):
    def test_create(self):
        Base.metadata.drop_all()
        Base.metadata.create_all()

    def test_add(self):
        m1 = Menu()
        m1.title = '用户管理'

        session.add(m1)
        session.commit()

    def test_adds(self):
        session.add_all([
            Menu(title='订单管理'),
            Menu(title='会员管理', url='/user1', parent_id=1),
            Menu(title='派件员', url='/user2', parent_id=1),
            Menu(title='合作商', url='/user3', parent_id=1),
            Menu(title='订单统计', url='/order_cnt', parent_id=2),
        ])
        session.commit()

    def test_get(self):
        m = session.query(Menu).get(1)
        print(m.title)
        for cm in m.childs:
            print(cm)

    def test_query_root_menu(self):
        ms = session.query(Menu).filter(Menu.parent_id.is_(None)).all()
        for menu in ms:
            print(menu)
            for secondary in menu.childs:
                print('-'*3,secondary)

    def test_update(self):
        menu = session.query(Menu).get(5)
        menu.title = '合作伙伴'
        session.commit()

    def test_remove(self):
        menu = session.query(Menu).get(5)
        session.delete(menu)
        session.commit()
