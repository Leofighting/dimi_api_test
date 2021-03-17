import allure
import pytest

from api.pending_request_api import PendingRequest
from api.purchase_apply_api import PurchaseApply
from api.purchase_order_api import PurchaseOrder


@allure.feature("测试采购订单模块")
class TestPurchaseOrder:
    def setup_class(self):
        self.purchase_order = PurchaseOrder()
        self.purchase_apply = PurchaseApply()
        self.pending_request = PendingRequest()

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

    @allure.story("测试提交采购订单")
    def test_purchase_order_submit(self):
        """
        测试 提交采购订单
        :return:
        """
        # 保存申购单，获取返回的响应信息
        purchase_apply_response = self.purchase_apply.purchase_apply_save()
        # 获取申购单id，单号
        purchase_apply_id, purchase_apply_order_no = (
            purchase_apply_response["data"]["id"],
            purchase_apply_response["data"]["orderNo"],
        )
        # 提交申购单
        self.purchase_apply.purchase_apply_submit(
            purchase_apply_id, purchase_apply_order_no
        )
        # 获取采购订单id
        purchase_order_id = self.pending_request.create_purchase_order(
            purchase_apply_order_no
        )["data"][0]["id"]
        # 提交采购订单
        r = self.purchase_order.purchase_order_submit(purchase_order_id)
        # 断言
        assert r["msg"] == "提交成功"
        assert r["success"] is True
