import allure
import pytest

from api.pending_request_api import PendingRequest
from api.purchase_apply_api import PurchaseApply


@allure.feature("测试待处理请求模块")
class TestPendingRequest:
    def setup_class(self):
        self.purchase_apply = PurchaseApply()
        self.pending_request = PendingRequest()

    @allure.story("测试生成采购订单")
    def test_create_purchase_order(self):
        """
        测试生成采购订单
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
        r = self.pending_request.create_purchase_order(purchase_apply_order_no)
        # 断言
        assert r["msg"] == "保存成功"
        assert r["success"] is True
        assert r["data"][0]["poCode"] is not None

    @allure.story("测试指定旧物料")
    def test_change_to_old_material(self):
        """
        测试指定旧物料
        :return:
        """
        r = self.pending_request.change_to_old_material()
        assert r["msg"] == "保存成功"
        assert r["success"] is True

    @allure.story("测试修改供应商功能")
    def test_update_supplier(self):
        """
        测试修改供应商
        :return:
        """
        r = self.pending_request.update_supplier()
        assert r["msg"] == "修改成功"
        assert r["success"] is True

    @allure.story("测试修改购买备注")
    def test_update_remark(self):
        """
        测试修改购买备注
        :return:
        """
        r = self.pending_request.update_remark()
        assert r["msg"] == "修改成功"
        assert r["success"] is True

    @allure.story("测试同步标识灯功能")
    def test_synchronize(self):
        """
        测试 同步标识灯 功能
        :return:
        """
        r = self.pending_request.synchronize()
        assert r["msg"] == "同步更新申购单红、绿、蓝灯状态成功"
        assert r["success"] is True

    @allure.story("测试采购关闭")
    def test_purchase_apply_close(self):
        """
        测试采购关闭功能
        :return:
        """
        r = self.pending_request.purchase_apply_close()
        assert r["msg"] == "关闭成功"
        assert r["success"] is True

    @allure.story("测试重新开启")
    def test_restart(self):
        """
        测试重新开启
        :return:
        """
        r = self.pending_request.restart()
        assert r["msg"] == "查询成功"
        assert r["success"] is True
