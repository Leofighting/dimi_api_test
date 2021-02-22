from api.purchase_order_api import PurchaseOrder


class TestPurchaseOrder:
    def setup_class(self):
        self.purchase_order = PurchaseOrder()

    def test_purchase_order_search_by_supCode(self):
        """
        采购订单：测试通过供应商编码查询采购订单
        :return:
        """
        r = self.purchase_order.purchase_order_search_by_supCode()
        # print(len(r["data"]["list"]))
        assert r["msg"] == "查询成功"
        assert r["success"] is True
        assert len(r["data"]["list"]) > 0
