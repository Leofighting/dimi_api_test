import allure
import pytest

from api.order_follow_api import OrderFollow


@allure.feature("测试发货单")
class TestOrderFollow:
    def setup_class(self):
        self.order_follower = OrderFollow()

    @allure.story("测试 通过物料编码查询发货单")
    @pytest.mark.parametrize("mat_code", ["146006", "60001", "10026", "14600600010026"])
    def test_order_detail_search_by_matCode(self, mat_code):
        r = self.order_follower.order_detail_search_by_matCode(mat_code)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0

    @allure.story("测试 对状态为-B2B已退回的订单，进行关闭明细，并释放")
    def test_close_return_detail_and_release(self):
        r = self.order_follower.close_return_detail_and_release()
        assert r["msg"] == "关闭成功"
        assert r["success"] is True