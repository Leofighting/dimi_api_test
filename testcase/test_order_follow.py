import allure
import pytest

from api.order_follow_api import OrderFollow


@allure.feature("测试发货单")
class TestOrderFollow:
    def setup_class(self):
        self.order_follower = OrderFollow()

    @allure.story("测试 通过物料编码查询发货单")
    @pytest.mark.parametrize("matCode", ["146006", "60001", "10026", "14600600010026"])
    def test_order_detail_search_by_matCode(self, matCode):
        r = self.order_follower.order_detail_search_by_matCode(matCode)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0
