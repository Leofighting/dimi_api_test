import allure
import pytest

from api.B2B_purchase_order_api import B2BPurchaseOrder
from api.pending_request_api import PendingRequest
from api.purchase_apply_api import PurchaseApply
from api.purchase_order_api import PurchaseOrder


@allure.feature("测试B2B-采购订单模块")
class TestB2BPurchaseOrder:
    def setup(self):
        self.purchase_order = PurchaseOrder()
        self.purchase_apply = PurchaseApply()
        self.pending_request = PendingRequest()
        self.B2B_purchase_order = B2BPurchaseOrder()

    @allure.story("测试供应商查询采购订单")
    @pytest.mark.parametrize("order_no", ["PO", "21"])
    def test_purchase_order_search_by_no(self, order_no):
        """
        通过采购订单号查询
        :param order_no: 采购订单号
        :return:
        """
        r = self.B2B_purchase_order.purchase_order_search_by_no(order_no)
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0

    @allure.story("测试供应商确认采购订单")
    def test_receive_purchase_order(self):
        """
        测试供应商对订单进行 订单确认 操作
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
        # 生成采购订单
        purchase_order = self.pending_request.create_purchase_order(
            purchase_apply_order_no
        )
        # 获取采购订单id，采购订单号
        purchase_order_id, purchase_order_no = (
            purchase_order["data"][0]["id"],
            purchase_order["data"][0]["poCode"],
        )
        # 提交采购订单
        self.purchase_order.purchase_order_submit(purchase_order_id)
        # 获取采购订单明细 ids，用于订单确认
        ids = self.B2B_purchase_order.get_ids(purchase_order_no)
        # 供应商订单确认
        r = self.B2B_purchase_order.receive_purchase_order(ids)
        # print(purchase_order_no)
        # 断言
        assert r["msg"] == "处理成功"
        assert r["success"] is True

    @allure.story("测试供应商退回采购订单")
    def test_receive_purchase_order(self):
        """
        测试供应商对订单进行 订单退回 操作
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
        # 生成采购订单
        purchase_order = self.pending_request.create_purchase_order(
            purchase_apply_order_no
        )
        # 获取采购订单id，采购订单号
        purchase_order_id, purchase_order_no = (
            purchase_order["data"][0]["id"],
            purchase_order["data"][0]["poCode"],
        )
        # 提交采购订单
        self.purchase_order.purchase_order_submit(purchase_order_id)
        # 获取采购订单明细 ids，用于订单退回
        ids = self.B2B_purchase_order.get_ids(purchase_order_no)
        # 供应商订单确认
        r = self.B2B_purchase_order.return_purchase_order(ids)
        print(purchase_order_no)
        # 断言
        assert r["msg"] == "处理成功"
        assert r["success"] is True
