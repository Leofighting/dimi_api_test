from api.order_follow_api import OrderFollow


class TestOrderFollow:
    def setup_class(self):
        self.order_follower = OrderFollow()

    def test_order_detail_search_by_matCode(self):
        r = self.order_follower.order_detail_search_by_matCode()
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0
