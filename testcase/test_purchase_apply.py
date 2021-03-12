import allure
import pytest

from api.purchase_apply_api import PurchaseApply


@allure.feature("测试申购单模块")
class TestPurchaseApply:
    def setup_class(self):
        self.purchase_apply = PurchaseApply()

    @allure.story("测试申购单复制")
    @pytest.mark.parametrize(
        "order_no",
        [
            "211-PR2103050011",
            "211-PR2103050017",
            "211-PR2103050009",
            "211-PR2101060001",
        ],
        ids=("状态-草稿", "状态-采购中", "状态-已提交待采购", "状态-已完成"),
    )
    def test_purchase_apply_copy(self, order_no):
        """
        测试申购单复制：分别按照不同状态的申购单进行复制
        :return:
        """
        r = self.purchase_apply.purchase_apply_copy(order_no)
        print(r)
        assert r["msg"] == "复制成功"
        assert r["success"] is True

    def test_purchase_apply_save(self):
        """
        测试保存申购单
        :return:
        """
        r = self.purchase_apply.purchase_apply_save()
        assert r["msg"] == "保存成功"
        assert r["success"] is True
        assert r["data"]["orderNo"] is not None

    def test_purchase_apply_submit(self):
        """
        测试提交申购单
        :return:
        """
        # 保存申购单，获取返回的响应信息
        purchase_apply_response = self.purchase_apply.purchase_apply_save()
        # 获取申购单id，单号
        purchase_apply_id, purchase_apply_order_no = (
            purchase_apply_response["data"]["id"],
            purchase_apply_response["data"]["orderNo"],
        )
        r = self.purchase_apply.purchase_apply_submit(
            purchase_apply_id, purchase_apply_order_no
        )
        assert r["msg"] == "保存成功"
        assert r["success"] is True
        assert r["data"]["orderNo"] is not None
        assert r["data"]["status"] == "WaitPurchase"

