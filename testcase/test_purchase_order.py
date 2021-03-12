import allure
import pytest

from api.purchase_order_api import PurchaseOrder


@allure.feature("测试采购订单模块")
class TestPurchaseOrder:
    def setup_class(self):
        self.purchase_order = PurchaseOrder()

    @allure.story("测试通过供应商编号查询采购订单")
    @pytest.mark.parametrize("sup_code", ["0101981", "0101", "019", "981"])
    def test_purchase_order_search_by_supCode(self, sup_code):
        """
        采购订单：测试通过供应商编码查询采购订单
        :return:
        """
        r = self.purchase_order.purchase_order_search_by_supCode(sup_code)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0
